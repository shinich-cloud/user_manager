import hashlib
from storage import load_users, save_users
from audit_log import write_log

ROLES = ("user", "moderator", "admin")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register(username: str, password: str) -> None:
    users = load_users()

    if any(u["username"] == username for u in users):
        print("❌ Пользователь уже существует")
        return

    role = "admin" if not users else "user"

    user = {
        "id": len(users) + 1,
        "username": username,
        "password": hash_password(password),
        "role": role
    }

    users.append(user)
    save_users(users)
    write_log(username, "register")

    print(f"✅ Пользователь зарегистрирован (роль: {role})")


def login(username: str, password: str):
    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed:
            write_log(username, "login")
            print(f"🎉 Вход выполнен. Роль: {user['role']}")
            return user

    print("❌ Неверный логин или пароль")
    return None


def list_users(current_user: dict) -> None:
    if current_user["role"] not in ("admin", "moderator"):
        print("⛔ Доступ запрещён")
        return

    for user in load_users():
        print(f"{user['id']}. {user['username']} ({user['role']})")


def set_role(current_user: dict, user_id: int, role: str) -> None:
    if current_user["role"] != "admin":
        print("⛔ Только admin может менять роли")
        return

    if role not in ROLES:
        print("❌ Недопустимая роль")
        return

    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user["role"] = role
            save_users(users)
            write_log(current_user["username"], "change_role", user["username"])
            print("✅ Роль обновлена")
            return

    print("❌ Пользователь не найден")
