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

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "password": hash_password(password),
        "role": "user"
    }

    users.append(new_user)
    save_users(users)
    print("✅ Пользователь зарегистрирован")


def login(username: str, password: str) -> None:
    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed:
            print(f"🎉 Вход выполнен. Роль: {user['role']}")
            return

    print("❌ Неверный логин или пароль")


def list_users() -> None:
    users = load_users()
    if not users:
        print("📭 Пользователей нет")
        return

    for user in users:
        print(f"{user['id']}. {user['username']} ({user['role']})")