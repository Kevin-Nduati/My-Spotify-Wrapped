from airflow import models, settings
import os
from dotenv import load_dotenv

load_dotenv()


db_uri = settings.SQL_ALCHEMY_CONN


conn = models.Connection(
    conn_id="spotify_conn_id",
    conn_type="http",
    host="https://api.spotify.com/v1",
    login=os.getenv("client_id"),
    password=os.getenv("client_secret"),
)

session = settings.Session()
session.add(conn)
session.commit()
