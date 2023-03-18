Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


### Dbt Objective
I want to create summary statistics that will explain more about my music taste. I currently have the following columns collected from songs:
* track_id
* track_name
* album_id
* release_date
* artist_id
* artist_name
* song_duration_ms
* explicit
* popularity
* played_at


Some of the macros i will create are:
* **spotify_wrapped__get_time_period** - This macro will take in a start and end date and return a list of time periods (e.g. weeks, months) between those two dates.
* **spotify_wrapped__get_most_streamed_songs** - This macro will take in a time period and return the most streamed songs during that period.
* **spotify_wrapped__get_most_streamed_artists** - This macro will take in a time period and return the most streamed artists during that period.
* **spotify_wrapped__get_total_minutes_streamed** - This macro will take in a time period and return the total number of minutes streamed during that period.
* **spotify_wrapped__get_music_preference** - This macro will take in a time period and return a breakdown of music listened to by time and day of the week.
* **spotify_wrapped__get_song_preference_by_duration** - This macro will take in a time period and return a breakdown of song preference depending on the duration of the song.
* **spotify_wrapped__get_release_dates** - This macro will take in a time period and return a breakdown of music release dates.
* **spotify_wrapped__get_popularity_of_songs** - This macro will take in a time period and return a breakdown of the popularity of songs listened to.
* **spotify_wrapped__get_number_of_artists_listened_to** - This macro will take in a time period and return the number of artists listened to.
* **spotify_wrapped__get_number_of_songs_listened_to** - This macro will take in a time period and return the number of songs listened to.


Some of the models i will create are:
tracks - This model will be based on the tracks table in our database, and will represent the raw data from the Spotify API.
time_periods - This model will use the spotify_wrapped__get_time_period macro to generate a list of time periods between two dates.
most_streamed_songs - This model will use the spotify_wrapped__get_most_streamed_songs macro to return the most streamed songs during a specified time period.
most_streamed_artists - This model will use the spotify_wrapped__get_most_streamed_artists macro to return the most streamed artists during a specified time period.
total_minutes_streamed - This model will use the spotify_wrapped__get_total_minutes_streamed macro to return the total number of minutes streamed during a specified time period.
music_preference - This model will use the spotify_wrapped__get_music_preference macro to return a breakdown of music listened to by time and day of the week during a specified time period.
song_preference_by_duration - This model will use the spotify_wrapped__get_song_preference_by_duration macro to return a breakdown of song preference depending on the duration of the song during a specified time period.
release_dates - This model will use the spotify_wrapped__get_release_dates macro to return a breakdown of music release dates during a specified time period.
popularity_of_songs - This model will use the spotify_wrapped__get_popularity_of_songs macro to return a breakdown of the popularity of songs listened to during a specified time period.
number_of_artists_listened_to - This model will use the spotify_wrapped__get_number_of_artists_listened_to macro to return the number of artists listened to during a specified time period.
number_of_songs_listened_to - This model will use the spotify_wrapped__get_number_of_songs_listened_to macro to return the number of songs listened to during a specified time period.


Here are some potential metrics that we could define for this project:

most_streamed_songs_count: This metric will count the number of rows in the most_streamed_songs model. This will allow us to track the number of most-streamed songs over time.
most_streamed_artists_count: This metric will count the number of rows in the most_streamed_artists model. This will allow us to track the number of most-streamed artists over time.
total_minutes_streamed_sum: This metric will sum up the total_minutes_streamed column in the total_minutes_streamed model. This will allow us to track the total minutes streamed over time.
distinct_tracks_count: This metric will count the number of distinct track_id values in the tracks table. This will allow us to track the number of unique tracks in our data.
distinct_artists_count: This metric will count the number of distinct artist_id values in the tracks table. This will allow us to track the number of unique artists in our data.
distinct_albums_count: This metric will count the number of distinct album_id values in the tracks table. This will allow us to track the number of unique albums in our data.
total_streams_sum: This metric will sum up the popularity column in the tracks table. This will allow us to track the total number of times each track has been streamed.
number_of_artists_listened_to_count: This metric will count the number of rows in the number_of_artists_listened_to model. This will allow us to track the number of unique artists listened to over time.
number_of_songs_listened_to_count: This metric will count the number of rows in the number_of_songs_listened_to model. This will allow us to track the number of unique songs listened to over time.

