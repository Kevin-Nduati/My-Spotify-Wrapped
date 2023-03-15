# My-Spotify-Wrapped
The project aimed to create a personalized version of Spotify Wrapped, which summarizes a user's listening history for the year. The project used airflow for orchestration, Docker for containerization, dbt for modeling and transforming data, and GitHub Actions for continuous integration and delivery. The goal was to extract the user's listening history data from Spotify's API, transform it, and load it into a database. The transformed data would then be used to generate personalized insights and visualizations summarizing the user's listening history. The project aimed to provide a fun and engaging way for users to reflect on their musical tastes and preferences over time.
## Using the Spotify API
The available list of endpoints can be found here: <a href="https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album">endpoints</a>
In order to get access to the spotify api, you need to follow the following steps:
* Go to the Developers site: https://developer.spotify.com/dashboard/applications, create an app and copy the client id and the client secret.
* The client id and client secret will be used to access tokens and refresh tokens. The access token will expire after each hour so we will need to generate a new one each time using the refresh token.



