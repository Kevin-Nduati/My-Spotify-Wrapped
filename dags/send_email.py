import os
import base64


from airflow.operators.email import EmailOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

spotify_wrapped_image = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "operators/dashboard",
          "spotify_wrapped.png"
    )
)
dashboard = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "operators", "dashboard",
          "dashboard.py"
    )
)
print(dashboard)
with open(spotify_wrapped_image, "rb") as f:
    image_content = f.read()
    image_base64 = base64.b64encode(image_content).decode("utf-8")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["nduatikevin1@gamil.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=0.25),
}

dag = DAG(
    "spotify_wrapped_email",
    default_args=default_args,
    description="Your spotify wrapped for the past week",
    schedule_interval=timedelta(weeks=1),
    start_date=days_ago(1),
    catchup=False,
)

run_dashboard = BashOperator(
    task_id="run_dashboard", bash_command="python3 '{0}'".format(dashboard),
      dag=dag
)

dashboard = os.path.abspath(
    os.path.join(
    os.path.dirname(__file__), "..", "operators", "dashboard", "dashboard.py"
    )
)


send_email_notification = EmailOperator(
    task_id="send_email",
    to="nduatikevin1@gmail.com",
    subject="Your Spotify Wrapped for the past week",
    files=[spotify_wrapped_image],
    html_content="""
    <h2>Hey, There!!</h2>
    Here is your Spotify Wrapped for the past week.<br><br>
    <img src='cid:spotify_wrapped.png', height="2000px", width="2000px">
    """,
    dag=dag,
)

run_dashboard >> send_email_notification
