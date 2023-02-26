import json
import psycopg2
from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_json_to_postgres(filepath: str, tableName: str, databaseName: str, postgres_conn_id: str, *args, **kwargs):
    # load the data from json
    with open(filepath, "r") as f:
        data = json.load(f)

    # insert the data
    def insert_data(data):
        # connect to the postgres database
        hook = PostgresHook(postgres_conn_id=postgres_conn_id)
        conn = hook.get_conn()
        cur = conn.cursor()


        for row in data:
            cur.execute(
                f"""
                INSERT INTO {tableName} (name, id, artist_name, artist_id, release_date, popularity)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (row["name"], row["id"], row["artist_name"], row["artist_id"], row["release_date"], row["popularity"])
            )

        conn.commit()
        cur.close()
        conn.close()


    insert_data(data)