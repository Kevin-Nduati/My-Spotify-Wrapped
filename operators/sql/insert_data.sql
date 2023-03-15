INSERT INTO tracks (track_id, track_name, album_id, artist_id, song_duration_ms, is_explicit, popularity, played_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    INSERT INTO albums (album_id, album_name, release_date)
    VALUES (%s, %s, %s);
    INSERT INTO artists (artist_id, artist_name)
    VALUES (%s, %s)