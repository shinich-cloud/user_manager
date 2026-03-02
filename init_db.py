from db import get_conn

def main():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(open("schema.sql", "r", encoding="utf-8").read())
        conn.commit()
    print("OK")

if __name__ == "__main__":
    main()
