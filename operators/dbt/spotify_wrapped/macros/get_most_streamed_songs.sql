{% macro get_most_streamed_songs(start_date, end_date, limit) %}

SELECT 
    track_id,
    track_name,
    COUNT(track_id) as streams
FROM tracks
WHERE played_at BETWEEN '{{ start_date }}' and '{{ end_date }}'
GROUP BY track_id, track_name
ORDER BY streams DESC
LIMIT {{ limit }}

{% endmacro %}



