{{ test_macros('macros/format_track_name.sql') }}
{% set track_name = 'My Song (feat. Artist)' %}

SELECT 
    {{ format_track_name }} AS formatted_track_name