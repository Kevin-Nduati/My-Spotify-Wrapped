{% macro format_track_name(track_name) %}

    {{track_name | replace('feat', '') | replace('ft', '') | replace('(', '') | replace(')', '') | replace('[', '') | replace(']', '') | replace('{', '') | replace('}', '') | replace(':', '') | replace(',', '') | replace('.', '') | replace('/', '') | replace('\\', '') | replace('&', 'and') | replace('-', '') | trim }}

{% endmacro %}