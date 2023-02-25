--hacky way to do a create or replace
--this is in case we are rebuilding the project from scratch whenever the spotify genres table doesn't exist yet since it's doing a full refresh each run
create table if not exists spotify_genres (
    artist_id text,
    artist_name text,
    artist_genre text,
    last_updated_datetime_utc timestamp,
    primary key (artist_id)
);
drop table spotify_genres;
create table if not exists spotify_genres (
    artist_id text,
    artist_name text,
    artist_genre text,
    last_updated_datetime_utc timestamp,
    primary key (artist_id)
);