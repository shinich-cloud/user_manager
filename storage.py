from db import get_conn

def get_all_users() -> list[dict]:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, password, role FROM users ORDER BY id")
            rows = cur.fetchall()
    return [{"id": r[0], "username": r[1], "password": r[2], "role": r[3]} for r in rows]

def get_user_by_username(username: str) -> dict | None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, password, role FROM users WHERE username=%s", (username,))
            r = cur.fetchone()
    if not r:
        return None
    return {"id": r[0], "username": r[1], "password": r[2], "role": r[3]}

def insert_user(username: str, password_hash: str, role: str) -> dict:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s) RETURNING id, username, password, role",
                (username, password_hash, role),
            )
            r = cur.fetchone()
        conn.commit()
    return {"id": r[0], "username": r[1], "password": r[2], "role": r[3]}

def update_user_role(user_id: int, role: str) -> dict | None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET role=%s WHERE id=%s RETURNING id, username, password, role",
                (role, user_id),
            )
            r = cur.fetchone()
        conn.commit()
    if not r:
        return None
    return {"id": r[0], "username": r[1], "password": r[2], "role": r[3]}
