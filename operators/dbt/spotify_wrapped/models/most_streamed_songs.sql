{{
    config(
        materialized = "view"
    )
}}

{{ get_most_streamed_songs(start_date=var('start_date'), end_date = var('end_date')) }}