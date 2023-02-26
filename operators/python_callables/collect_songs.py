from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import Variable, XCom
from datetime import datetime, timedelta
import requests
import json
import os
from refresh import RefreshToken



class RetrieveSongs:
    def __init__(self, filepath):
        self.user_id = os.getenv("spotify_username")  # Spotify username
        self.spotify_token = ""  # Spotify access token
        self.file_path = filepath  # File path to save JSON file
        

    def collect_kenyan_songs(self):
        url = "https://api.spotify.com/v1/search?limit=50"
        params = (
            ('q', "Kenya"), #popularity:>30
            ('type', "track")
        )
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_token}"
        }
        data = []
        song_count = 0
        while song_count < 570:
            response = requests.get(url, params=params, headers=headers)
            response_data = response.json()
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
                song_count += 1
                if song_count == 570:
                    break
            if response_data["tracks"]["next"]:
                params = None
                url = response_data["tracks"]["next"]
            else:
                break
            
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

        
            
    def call_refresh(self, **context):
        refresh_token = os.getenv("refresh_token")
        base_64 = os.getenv("base_64")
        refresher = RefreshToken(refresh_token, base_64)
        self.spotify_token = refresher.refresh()
        self.collect_kenyan_songs()

        



if __name__ =="__main__":
    cwd = "/home/kevin/Desktop/Github projects/My-Spotify-Wrapped/operators"
    filepath = os.path.join(cwd, "kenyan_songs.json")
    tracks = RetrieveSongs(filepath)
    tracks.call_refresh()
    print(len)
    



  


