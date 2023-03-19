CREATE TABLE tracks(
  id SERIAL PRIMARY KEY,
  track_id TEXT,
  track_name TEXT,
  album_id TEXT,
  artist_id TEXT,
  song_duration_ms INTEGER,
  is_explicit BOOLEAN,
  popularity INTEGER,
  played_at TIMESTAMP
);



CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  album_id TEXT UNIQUE,
  album_name TEXT,
  release_date TEXT
);

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  artist_id  TEXT UNIQUE,
  artist_name TEXT,
  genres TEXT

)

