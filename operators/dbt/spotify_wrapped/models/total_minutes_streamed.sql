{{
    config(
        materialized = "view"
    )
}}


{{ get_total_minutes_streamed(start_date="2023-01-01", end_date = "2023-04-01")}}