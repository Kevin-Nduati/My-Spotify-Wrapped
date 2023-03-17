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

Some of the tables/views that we need are:
* get the most-streamed songs
* get the most streamed artists
* total minutes streamed
* aggregate music listened to depending on the time and day
* check preference of songs depending on the duration
* analyze music release dates
* popularity of songs
* how many artists i listen to
* how many songs i listen to


Let us analyze what exactly is needed and what aggregations and summary tables will be created:
#### Music Depending on the time and day
