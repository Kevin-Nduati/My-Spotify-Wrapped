import sys
import os
# Get the parent directory of the current file (which should be the "dags" folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Add the "operators" folder to the Python path
operators_folder = os.path.join(parent_dir, "operators")
sys.path.append(operators_folder)

collect_songs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'operators/python_callables', 'collect_songs.py'))
insert_songs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'operators/python_callables', 'insert_songs.py'))

cwd = "/home/kevin/Desktop/Github projects/My-Spotify-Wrapped/operators"
filepath = os.path.join(cwd, "kenyan_songs.json")



from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.slack.hooks import slack_webhook
from airflow.hooks.base import BaseHook
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

# import refresh
from collect_songs import RetrieveSongs
from insert_songs import load_json_to_postgres
# insert_spotify_data_to_postgres

from airflow.providers.http.operators.http import SimpleHttpOperator
# from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.hooks.postgres import PostgresHook

from datetime import datetime, timedelta
import json
import os
import requests
import logging
import postgres_connect
postgres_connection = postgres_connect.ConnectPostgres().postgres_connector()




default_args = {
    "owner": "Kevin Nduati", 
    "depends_on_past": False,
    "start_date": datetime(2023, 2, 25),
    "email_on_retry": False,
    "email_on_failure": False,
    "retries": 4,
    "retry_delay": timedelta(minutes=0.5)

}

dag = DAG(
    "spotify_kenyan",
    default_args=default_args,
    start_date=datetime(2023,2,2),
    schedule_interval="@once"
)


      

collect_data = BashOperator(
    task_id = "extract_spotify_data",
    bash_command='python3 "{0}"'.format(collect_songs),
    dag = dag
)


load_data = PythonOperator(
    task_id = "load_data",
    python_callable=load_json_to_postgres,
    op_kwargs={
        "filepath": filepath,
        "tableName": "public.spotify_kenyan_data",
        "databaseName": "spotify",
        "postgres_conn_id": "postgres_conn"
    }
)


collect_data >> load_data










### saved
# def insert_spotify_data_to_postgres(**context):
#     pg_hook = PostgresHook("postgres_connection")
#     spotify_data = context["ti"].xcom_pull(key="spotify_data", task_ids="collect_spotify_data")
#     for item in spotify_data:
#         query = """
#         INSERT INTO spotify_kenyan_data (name, track_id, artist_name, artist_id, release_date, popularity)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """
#         pg_hook.run(
#             query,
#             parameters=(item["name"], item["id"], item["artist_name"], item["artist_id"], item["release_date"], item["popularity"])
#         )
