"""
Makes requests to the Spotify API to retrieve recently played songs and their corresponding genres
"""

import datetime as dt
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import requests
from postgres_connect import ConnectPostgres
from refresh import RefreshToken
from yaml_load import yaml_loader


class RetrieveSongs:
    def __init__(self):
        self.user_id = os.getenv("spotify_username")
        self.spotify_token = os.getenv("access_token")

    # get the latest played timestamp
    conn = ConnectPostgres.postgres_connector()
    cur = conn.cursor()

    query = "SELECT MAX(played_at_utc) FROM public.spotify_songs"

    cur.execute(query)
    max_played_at_utc = cur.fetchall()[0][0]

    
            
