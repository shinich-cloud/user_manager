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
                username = input("Имя пользователя: ")
                password = input("Пароль: ")
                register(username, password)

            elif choice == "2":
                username = input("Имя пользователя: ")
                password = input("Пароль: ")
                current_user = login(username, password)

            elif choice == "0":
                print("👋 Пока!")
                break

        else:
            print(f"\n--- Меню ({current_user['role']}) ---")
            print("1. Список пользователей (admin)")
            print("2. Назначить роль (admin)")
            print("3. Выйти из аккаунта")

            choice = input("Выбор: ")

            if choice == "1":
                list_users(current_user)

            elif choice == "2":
                user_id = int(input("ID пользователя: "))
                role = input("Новая роль (user/admin): ")
                set_role(current_user, user_id, role)

            elif choice == "3":
                current_user = None


if __name__ == "__main__":
    main()
