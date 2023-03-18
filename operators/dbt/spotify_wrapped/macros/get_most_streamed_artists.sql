{% macro get_most_streamed_artists(start_date, end_date, limit) %}

-- fix it

SELECT 
   t.artist_id,
   a.artist_name,
   COUNT(DISTINCT t.artist_id) AS streams

FROM tracks AS t
join artists AS a
USING (artist_id)
WHERE played_at BETWEEN '{{ start_date }}' AND '{{ end_date }}'
GROUP BY a.artist_name, t.artist_id
ORDER BY streams  DESC
LIMIT {{ limit }}

{% endmacro %}