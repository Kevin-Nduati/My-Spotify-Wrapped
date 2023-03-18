{{
    config(
        materialized = "view"
    )
    
}}

{{ get_minutes_per_artists(start_date="2023-01-01", end_date = "2023-04-01",limit=10)}}