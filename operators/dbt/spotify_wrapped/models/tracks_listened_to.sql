{{
    config(
        materialized="view"
    )
}}

{{ get_tracks_listened_to(start_date=var('start_date'), end_date = var('end_date')) }}