{% macro get_tracks_per_dow(start_date, end_date) %}

SELECT EXTRACT(DOW FROM played_at) AS day_of_week, 
    EXTRACT(HOUR FROM played_at) AS hour,
    SUM(SONG_duration_ms / (60 * 100)) AS total_minutes
from public.tracks
WHERE played_at BETWEEN '{{ start_date }}' AND '{{ end_date }}'
GROUP BY day_of_week, hour
ORDER BY total_minutes DESC

{% endmacro %}
