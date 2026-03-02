import hashlib
from storage import get_all_users, get_user_by_username, insert_user, update_user_role
from audit_log import write_log

ROLES = ("user", "moderator", "admin")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register(username: str, password: str) -> None:
    if get_user_by_username(username):
        print("❌ Пользователь уже существует")
        return

    role = "admin" if len(get_all_users()) == 0 else "user"
    insert_user(username, hash_password(password), role)
    write_log(username, "register")
    print(f"✅ Пользователь зарегистрирован (роль: {role})")

def login(username: str, password: str):
    user = get_user_by_username(username)
    if user and user["password"] == hash_password(password):
        write_log(username, "login")
        print(f"🎉 Вход выполнен. Роль: {user['role']}")
        return user
    print("❌ Неверный логин или пароль")
    return None

def list_users(current_user: dict) -> None:
    if current_user["role"] not in ("admin", "moderator"):
        print("⛔ Доступ запрещён")
        return
    for user in get_all_users():
        print(f"{user['id']}. {user['username']} ({user['role']})")

def set_role(current_user: dict, user_id: int, role: str) -> None:
    if current_user["role"] != "admin":
        print("⛔ Только admin может менять роли")
        return
    if role not in ROLES:
        print("❌ Недопустимая роль")
        return
    updated = update_user_role(user_id, role)
    if updated:
        write_log(current_user["username"], "change_role", updated["username"])
        print("✅ Роль обновлена")
        return
    print("❌ Пользователь не найден")
