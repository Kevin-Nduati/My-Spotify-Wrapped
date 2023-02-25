import sys
sys.path.append("operators")
from datetime import datetime, timedelta

# from .operators 
import copy_to_postgres
from airflow import DAG
from airflow.providers.slack.hooks import slack_webhook
from airflow.hooks.base import BaseHook
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator


def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection("slack_conn").password
    slack_msg = """
    :X: Task Failed
    *Task*: {task}
    *Dag*: {dag}
    *Execution Time*: {exec_date}
    *Log URL*: {log_url}
    """.format(
        task = context.get("task_instance").task_id,
        dag = context.get("task_instance").dag_id,
        ti = context.get("task_instance"),
        exec_date = context.get("execution_date"),
        log_url = context.get("task_instance").log_url
    )

    failed_alert = SlackWebhookOperator(
        task_id = "slack_alert",
        http_conn_id = "slack_conn",
        webhook_token= slack_webhook_token,
        message= slack_msg,
        username = "airflow",
        dag = dag,
    )

    return failed_alert.execute(context=context)


args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 12),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "on_success_callback": None,
    "on_failure_callback": task_fail_slack_alert
   }

