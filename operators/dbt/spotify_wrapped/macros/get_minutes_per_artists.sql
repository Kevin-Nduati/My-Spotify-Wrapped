{% macro get_minutes_per_artists(start_date, end_date, limit) %}

SELECT 
    a.artist_name,
    SUM(t.song_duration_ms / (60*1000)) as minutes
FROM tracks AS t
JOIN artists AS a
USING (artist_id)
WHERE played_at BETWEEN '{{ start_date }}' AND '{{ end_date }}'
GROUP BY a.artist_name
ORDER BY minutes DESC
LIMIT {{ limit }}

{% endmacro %}