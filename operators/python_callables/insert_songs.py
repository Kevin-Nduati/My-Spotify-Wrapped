import json
import psycopg2
from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_json_to_postgres(data, databaseName: str, postgres_conn_id: str, *args, **kwargs):
    # connect to the postgres database
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = hook.get_conn()
    cur = conn.cursor()


    for row in data:
        cur.execute(
    """
    INSERT INTO tracks (track_id, track_name, album_id, artist_id, song_duration_ms, is_explicit, popularity, played_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    INSERT INTO albums (album_id, album_name, release_date)
    VALUES (%s, %s, %s);
    INSERT INTO artists (artist_id, artist_name)
    VALUES (%s, %s)
    """, (
        row["track_id"], row["track_name"], row["album_id"], row["artist_id"], row["song_duration_ms"], 
        row["explicit"], row["popularity"], row["played_at"], row["album_id"], row["album_name"], 
        row["release_date"], row["artist_id"], row["artist_name"]
    )
)


        conn.commit()
        # cur.close()
        # conn.close()
