{% macro get_newly_discovered_artists(start_date, end_date) %}

SELECT a.artist_name
FROM tracks AS t
JOIN artists AS a
USING(artist_id)
WHERE played_at >= '{{ start_date }}'
  AND artist_id NOT IN (
    SELECT artist_id
    FROM tracks
    WHERE played_at < '{{ start_date}}'
  )

{% endmacro %}
