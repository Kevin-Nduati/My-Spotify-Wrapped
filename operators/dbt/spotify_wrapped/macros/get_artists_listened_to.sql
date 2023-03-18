{% macro get_artists_listened_to(start_date, end_date) %}

SELECT COUNT(DISTINCT artist_id)
FROM tracks
WHERE played_at BETWEEN '{{ start_date }}'  AND '{{ end_date }}'

{% endmacro %}