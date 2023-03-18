{% macro get_tracks_listened_to(start_date, end_date) %}

SELECT COUNT(DISTINCT track_id)
FROM tracks
WHERE played_at BETWEEN '{{ start_date }}'  AND '{{ end_date }}'

{% endmacro %}