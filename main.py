from users import register, login, list_users, set_role


def main():
    current_user = None

    while True:
        if not current_user:
            print("\n--- User Manager ---")
            print("1. Регистрация")
            print("2. Вход")
            print("0. Выход")

            choice = input("Выбор: ")

            if choice == "1":
                register(input("Имя: "), input("Пароль: "))
            elif choice == "2":
                current_user = login(input("Имя: "), input("Пароль: "))
            elif choice == "0":
                break
        else:
            print(f"\n--- Меню ({current_user['role']}) ---")

            print("1. Выйти из аккаунта")

            if current_user["role"] in ("admin", "moderator"):
                print("2. Список пользователей")

            if current_user["role"] == "admin":
                print("3. Назначить роль")

            choice = input("Выбор: ")

            if choice == "1":
                current_user = None

            elif choice == "2" and current_user["role"] in ("admin", "moderator"):
                list_users(current_user)

            elif choice == "3" and current_user["role"] == "admin":
                set_role(
                    current_user,
                    int(input("ID пользователя: ")),
                    input("Новая роль (user/moderator/admin): ")
                )


if __name__ == "__main__":
    main()
