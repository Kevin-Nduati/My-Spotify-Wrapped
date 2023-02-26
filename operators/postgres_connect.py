from dotenv import load_dotenv
import os
load_dotenv()

import psycopg2


class ConnectPostgres:
    def __init__(self):
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.dbname = os.getenv("dbname")
        self.pg_user = os.getenv("pg_user")
        self.pg_password = os.getenv("pg_password")

    def postgres_connector(self):
        conn = psycopg2.connect(
            f"host='{self.host}' port='{self.port}' dbname='{self.dbname}' user='{self.pg_user}' password='{self.pg_password}'"

        )
        return conn


if __name__ == "__main__":
    conn = ConnectPostgres()
    conn.postgres_connector()