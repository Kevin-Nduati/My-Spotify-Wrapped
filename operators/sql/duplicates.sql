-- Add a constraint to prevent the duplication of data in the tracks table
ALTER TABLE tracks
ADD CONSTRAINT unique_track_info
UNIQUE (track_id, album_id, played_at);


