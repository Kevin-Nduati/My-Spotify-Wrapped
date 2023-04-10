{{
    config(
        materialized = "view"
    )
}}


{{ get_newly_discovered_artists(start_date=var('start_date'), end_date = var('end_date')) }}