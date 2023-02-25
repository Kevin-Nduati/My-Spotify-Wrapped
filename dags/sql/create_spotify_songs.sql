create table if not exists spotify_songs (
    played_at_utc timestamp,
    played_date_utc date,
    song_name text,
    artist_name text,
    song_duration_ms integer,
    song_link text,
    album_art_link text,
    album_name text,
    album_id text,
    artist_id text,
    track_id text,
    last_updated_datetime_utc timestamp,
    primary key (played_at_utc)
);