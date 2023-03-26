{{
    config(
        materialized = "view"
    )
}}

{{ get_tracks_per_dow(start_date=var('start_date'), end_date = var('end_date')) }}