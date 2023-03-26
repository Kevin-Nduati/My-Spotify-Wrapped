{{
    config(
        materialized = "view"
    )
    
}}

{{ get_minutes_per_artists(start_date=var('start_date'), end_date = var('end_date')) }}