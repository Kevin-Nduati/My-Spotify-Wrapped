from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import Variable, XCom
from datetime import datetime, timedelta
import requests
import json
import os
from refresh import RefreshToken
from dotenv import load_dotenv
load_dotenv()




def recently_played_songs(filepath):
    url = f"https://api.spotify.com/v1/me/player/recently-played?limit=5"
    # &after={start_time}&before={end_time}"
    params = {}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('access_token')}"
    }
    data = []
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        tracks = response_data["items"]
        for track in tracks:
            track_data = {
                "track_id": track["track"]["id"],
                "track_name": track["track"]["name"],
                "album_name": track["track"]["album"]["name"],
                "album_id": track["track"]["album"]["id"],
                "release_date": track["track"]["album"]["release_date"],
                "artist_id": track["track"]["artists"][0]["id"],
                "artist_name": track["track"]["artists"][0]["name"],
                "song_duration_ms": track["track"]["duration_ms"],
                "explicit": track["track"]["explicit"],
                "popularity": track["track"]["popularity"],
                "played_at": track["played_at"]
            }
        data.append(track_data)

        print("Success!!!!")

    else:
        print(f"{response.status_code}: Error Retrieving Spotify Data")
    
        
    with open(filepath, 'w') as f:
        json.dump(data, f)

        
    
    



  


