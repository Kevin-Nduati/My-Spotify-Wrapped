import json
import psycopg2
from airflow.providers.postgres.hooks.postgres import PostgresHook


def last_song(postgres_conn_id):
    # connect to the postgres database
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = hook.get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT MAX(played_at)
        FROM tracks
        """
    )
    result = cur.fetchone()[0]
    conn.commit()

    return result
