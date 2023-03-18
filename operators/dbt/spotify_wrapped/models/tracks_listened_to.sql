{{
    config(
        materialized="view"
    )
}}

{{ get_tracks_listened_to(start_date="2023-01-01", end_date = "2023-04-01")}}