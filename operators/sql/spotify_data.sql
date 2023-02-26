CREATE TABLE spotify_kenyan_data (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  track_id VARCHAR(255) NOT NULL,
  artist_name VARCHAR(255) NOT NULL,
  artist_id VARCHAR(255) NOT NULL,
  release_date DATE NOT NULL,
  popularity INTEGER NOT NULL
);