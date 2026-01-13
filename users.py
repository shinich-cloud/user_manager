from storage import load_users, save_users
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register(username: str, password: str) -> None:
    users = load_users()

    for user in users:
        if user["username"] == username:
            print("❌ Пользователь уже существует")
            return

    role = "admin" if len(users) == 0 else "user"

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "password": hash_password(password),
        "role": role
    }

    users.append(new_user)
    save_users(users)
    print(f"✅ Пользователь зарегистрирован (роль: {role})")


def login(username: str, password: str) -> dict | None:
    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed:
            print(f"🎉 Вход выполнен. Роль: {user['role']}")
            return user

    print("❌ Неверный логин или пароль")
    return None


def list_users(current_user: dict) -> None:
    if current_user["role"] != "admin":
        print("⛔️ Доступ запрещён (только admin)")
        return

    users = load_users()
    for user in users:
        print(f"{user['id']}. {user['username']} ({user['role']})")


def set_role(current_user: dict, user_id: int, role: str) -> None:
    if current_user["role"] != "admin":
        print("⛔️ Только admin может менять роли")
        return

    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user["role"] = role
            save_users(users)
            print("✅ Роль обновлена")
            return

    print("❌ Пользователь не найден")