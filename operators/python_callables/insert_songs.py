import json
import psycopg2
from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_json_to_postgres(data, databaseName: str, postgres_conn_id: str, *args, **kwargs):
    # connect to the postgres database
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = hook.get_conn()
    cur = conn.cursor()
    try:
        for row in data:
            # Insert or update row in the tracks table
            cur.execute(
                """
                INSERT INTO tracks (track_id, track_name, album_id, artist_id, song_duration_ms, is_explicit, popularity, played_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT ON CONSTRAINT unique_track_info
                DO NOTHING
                """,
                (row["track_id"], row["track_name"], row["album_id"], row["artist_id"], row["song_duration_ms"], 
                 row["explicit"], row["popularity"], row["played_at"])
            )
            # Insert or update row in the albums table
            cur.execute(
                """
                INSERT INTO albums (album_id, album_name, release_date)
                VALUES (%s, %s, %s)
                ON CONFLICT (album_id) DO NOTHING
                """,
                (row["album_id"], row["album_name"], row["release_date"])
            )
            # Insert or update row in the artists table
            cur.execute(
                """
                INSERT INTO artists (artist_id, artist_name, genres)
                VALUES (%s, %s, %s)
                ON CONFLICT (artist_id) DO NOTHING 
                """,
                (row["artist_id"], row["artist_name"], row["artist_genres"])
            )
            conn.commit()
        print(f"The insert procedure has been successfully run")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        cur.close()
        conn.close()

        
