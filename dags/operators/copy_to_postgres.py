"""
Copies the csvs to postgres
"""

from airflow.providers.postgres.hooks.postgres import PostgresHook

def copy_expert_csv(file):
    hook = PostgresHook("postgres_connection")
    with hook.get_conn() as connection:
        hook.copy_expert(
            f"""
            COPY {file} FROM stdin WITH CSV HEADER DELIMITER AS ','
            """,
            f"/airflow/dags/spotify_data/{file}.csv",
        )
        connection.commit()