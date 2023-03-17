{{ test_macros('macros/format_track_name.sql') }}
{% set track_name = 'My Song (feat. Artist)' %}

SELECT 
    {{ ref('format_track_name')(track_name) }} AS formatted_track_name