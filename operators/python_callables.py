from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import json
import os






def collect_kenyan_songs(**context):
    url = "https://api.spotify.com/v1/search?q=Kenya+popularity%3A%3E30&type=track&limit=50"
    data = data = []
    for i in range(20):
        response = SimpleHttpOperator(
            task_id = "Spotify_api_request_{}".format(i),
            http_conn_id="spotify_conn_id",
            endpoint = url,
            headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(os.getenv("access_token"))
            },
            method = "GET",
            response_check= lambda response: response.status_code == 200,
            dag = dag
        ).execute(context=context)
        response_data = json.loads(response.content)
        tracks = response_data["tracks"]["items"]
        for track in tracks:
            track_data = {
                "name": track["name"],
                "id": track["id"],
                "artist_name": track["artists"][0]["name"],
                "artist_id": track["artists"][0]["id"],
                "release_date": track["album"]["release_date"],
                "popularity": track["popularity"]
            }
            data.append(track_data)
        url = response_data["tracks"]["next"]
    context['ti'].xcom_push(key="spotify_data", value=data)



def insert_spotify_data_to_postgres(**context):
    pg_hook = PostgresHook("postgres_connection")
    spotify_data = context["ti"].xcom_pull(key="spotify_data", task_ids="collect_spotify_data")
    for item in spotify_data:
        query = """
        INSERT INTO spotify_data (name, track_id, artist_name, artist_id, release_date, popularity)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        pg_hook.run(
            query,
            parameters=(item["name"], item["id"], item["artist_name"], item["artist_id"], item["release_date"], item["popularity"])
        )
         


