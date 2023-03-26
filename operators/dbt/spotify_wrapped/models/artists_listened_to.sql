{{
    config(
        materialized="view"
    )
}}

{{ get_artists_listened_to(start_date=var('start_date'), end_date = var('end_date')) }}