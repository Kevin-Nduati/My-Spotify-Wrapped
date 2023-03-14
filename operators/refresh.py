"""
Generates a new access token on each run
"""

from dotenv import load_dotenv, set_key
load_dotenv()
import requests
import os
import base64
from urllib.parse import quote

refresh_token = os.getenv("refresh_token")
base_64 = os.getenv("base_64")
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(parent_dir+ "/.env")

import requests

class RefreshToken:
    def __init__(self, refresh_token, base_64):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(
            query,
            data = {"grant_type": "refresh_token", "refresh_token": self.refresh_token },
            headers = {"Authorization": "Basic " + self.base_64}
        )

        if response.status_code != 200:
            raise Exception("Request failed with status code: {}\nResponse: {}".format(
                response.status_code, response.text))

        response_json = response.json()
        if 'access_token' not in response_json:
            raise Exception("Response does not contain access_token field")

        return response_json['access_token']

if __name__=="__main__":
    new_token = RefreshToken(refresh_token, base_64)
    try:
        access_token = new_token.refresh()
        # os.environ["ACCESS_TOKEN"] = access_token
        set_key(dotenv_path = parent_dir+"/.env", key_to_set="access_token",value_to_set= access_token)
        print("Access token:", access_token)
    except Exception as e:
        print("Error:", str(e))
