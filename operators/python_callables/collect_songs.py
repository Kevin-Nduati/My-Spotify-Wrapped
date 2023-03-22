from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import Variable, XCom
from datetime import datetime, timedelta
import time
import requests
import json
import os
from refresh import RefreshToken
from dotenv import load_dotenv
load_dotenv()



def recently_played_songs(start_time):
    print(f"Start Date: {start_time}")
    url = f"https://api.spotify.com/v1/me/player/recently-played?limit=50&after={start_time}"
    url2 = "https://api.spotify.com/v1/artists?ids="
    params = {}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('access_token')}"
    }
    data = []
    response = requests.get(url, params=params, headers=headers)
    response_data = response.json()
    
    # have to make sure the output is not blank
    # hit second url for artist information
    if len(response_data['items']) != 0:
        print(f"There are {len(response_data['items'])} items in the dictionary")
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
            artist_url = url2 + track_data["artist_id"]
            response = requests.get(artist_url, headers=headers)
            response_data = response.json()
            track_data["artist_genres"] = response_data["artists"][0]["genres"]
            

            data.append(track_data)
            

        print(f"The operation has been successfully run!!!")
        return data


    else:
        print(f"No data was retrieved")
    
        
    

        
    
    



  


