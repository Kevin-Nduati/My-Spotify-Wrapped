{% macro get_total_minutes_streamed(start_date, end_date) %}

SELECT SUM(song_duration_ms / (60 * 1000)) AS total_minutes_streamed
FROM tracks
WHERE played_at BETWEEN '{{ start_date }}' AND '{{ end_date}}'

{% endmacro %}