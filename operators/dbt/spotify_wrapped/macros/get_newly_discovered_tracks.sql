{% macro get_newly_discovered_tracks(start_date, end_date) %}

SELECT DISTINCT(track_name)
FROM tracks
WHERE played_at >= '{{ start_date }}'
  AND track_id NOT IN (
    SELECT track_id
    FROM tracks
    WHERE played_at < '{{ start_date}}'
  )

{% endmacro %}