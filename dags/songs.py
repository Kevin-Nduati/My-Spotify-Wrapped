import os
import sys
import time
from datetime import date, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


# Get the parent directory of the current file ( "dags" folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "operators"))
)


refresh_token = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "operators", "refresh.py")
)
dbt_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "operators", "dbt", "spotify_wrapped")
)
import postgres_connect

postgres_connection = postgres_connect.ConnectPostgres().postgres_connector()
from python_callables.collect_songs import recently_played_songs
from python_callables.insert_songs import load_json_to_postgres
from python_callables.last_played_at import last_song


def get_next_execution_date():
    last_play_time = last_song(postgres_conn_id="postgres_conn")

    return last_play_time


def get_recently_played_songs(postgres_conn_id, **context):
    last_play_time = get_next_execution_date()
    execution_date = context["execution_date"]
    if last_play_time is None:
        date_string = execution_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"The database is empty. So we will use {date_string}")
        timestamp = int(time.mktime(time.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")))
        data = recently_played_songs(start_time=timestamp)
        ti = context["ti"]
        ti.xcom_push(key="my_data", value=data)
    else:
        date_string = last_play_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"The last played song is: {date_string}")
        timestamp = int(time.mktime(time.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")))
        data = recently_played_songs(start_time=timestamp)
        ti = context["ti"]
        ti.xcom_push(key="my_data", value=data)


def insert_data_from_xcom(databaseName, postgres_conn_id, **context):
    ti = context["ti"]
    data = ti.xcom_pull(key="my_data")
    load_json_to_postgres(
        data=data, databaseName=databaseName, postgres_conn_id=postgres_conn_id
    )


default_args = {
    "owner": "Kevin Nduati",
    "depends_on_past": False,
    # "start_date": start_time,
    "email_on_retry": False,
    "email_on_failure": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=0.5),
    "max_active_runs": 1,
    "execution_date_fn": get_next_execution_date,
}
# spotify does not store more than 50
dag = DAG(
    "my_spotify_wrapped",
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=timedelta(hours=3),  # you can define a cron job
)

get_access_token = BashOperator(
    task_id="get_access_token",
    bash_command="python3 '{0}'".format(refresh_token),
    dag=dag,
)


collect_songs_data = PythonOperator(
    task_id="collect_songs",
    python_callable=get_recently_played_songs,
    op_kwargs={"postgres_conn_id": "postgres_conn"},
    provide_context=True,
    dag=dag,
)


insert_data = PythonOperator(
    task_id="insert_data",
    python_callable=insert_data_from_xcom,
    op_kwargs={"databaseName": "spotify", "postgres_conn_id": "postgres_conn"},
    dag=dag,
)


end_date = date.today().strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")
dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="cd '"
    + dbt_folder
    + '\' && dbt run --vars \'{"start_date": "'
    + start_date
    + '", "end_date": "'
    + end_date
    + "\"}'",
)


dbt_test = BashOperator(
    task_id="dbt_test", bash_command=f"cd '{dbt_folder}' && dbt test"
)


# set up the dag procedure
get_access_token >> collect_songs_data >> insert_data >> dbt_run >> dbt_test
