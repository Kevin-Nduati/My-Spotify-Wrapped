import sys
import os

from airflow import DAG
from airflow.providers.slack.hooks import slack_webhook
from airflow.hooks.base import BaseHook
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta
import time


# Get the parent directory of the current file (which should be the "dags" folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'operators')))
import postgres_connect
from python_callables.collect_songs import recently_played_songs
from python_callables.insert_songs import *
filepath = os.path.join(parent_dir, "operators", "kenyan_songs.json")
refresh_token = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'operators', 'refresh.py'))
postgres_connection = postgres_connect.ConnectPostgres().postgres_connector()

# config
# start_time = datetime.now() - timedelta(days=10)
def get_recently_played_songs(filepath, **context):
    start_time = context["execution_date"] 
    start_time_unix_timestamp = int(start_time.timestamp())
    recently_played_songs(start_time=start_time_unix_timestamp, filepath=filepath)
    print(start_time)



default_args = {
    "owner": "Kevin Nduati", 
    "depends_on_past": False,
    # "start_date": start_time,
    "email_on_retry": False,
    "email_on_failure": False,
    "retries": 4,
    "retry_delay": timedelta(minutes=0.5)

}

dag = DAG(
    "spotify_wrapped1",
    default_args=default_args,
    start_date=days_ago(30),
    schedule_interval="@daily"
)

get_access_token = BashOperator(
    task_id  = "get_access_token",
    bash_command= "python3 '{0}'".format(refresh_token),
    dag = dag
)

      

collect_songs_data = PythonOperator(
    task_id = "collect_songs",
    python_callable= get_recently_played_songs,
    op_kwargs={
    "filepath": filepath
    },
    provide_context=True,
    dag = dag
)


# load_data = PythonOperator(
#     task_id = "load_data",
#     python_callable=load_json_to_postgres,
#     op_kwargs={
#         "filepath": filepath,
#         "tableName": "public.spotify_kenyan_data",
#         "databaseName": "spotify",
#         "postgres_conn_id": "postgres_conn"
#     }
# )


get_access_token >> collect_songs_data








