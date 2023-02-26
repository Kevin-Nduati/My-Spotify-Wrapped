import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json

headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(os.getenv("access_token"))
        }
params = (
    ('q', "Kenya popularity:>30"),
    ('type', "track")
)

url = "https://api.spotify.com/v1/search?limit=1"
# "https://api.spotify.com/v1/me/top/artists?limit=10"
# "https://api.spotify.com/v1/me/player/recently-played?limit=10"

headers = headers

response = requests.get(url, headers=headers, params=params)

if response.status_code != 200:
    print("Request failed with status code: {}".format(response.status_code))
else:
    response_json = response.json()
    with open('output.json', 'w') as file:
        json.dump(response_json, file)
