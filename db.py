import os
import psycopg2

def get_conn():
    host = os.getenv("PGHOST", "localhost")
    port = int(os.getenv("PGPORT", "5432"))
    dbname = os.getenv("PGDATABASE", "user_manager")
    user = os.getenv("PGUSER", "postgres")
    password = os.getenv("PGPASSWORD", "")
    return psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
