{{
    config(
        materialized = "view"
    )
}}


{{ get_total_minutes_streamed(start_date=var('start_date'), end_date = var('end_date')) }}