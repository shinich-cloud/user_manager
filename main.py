from users import register, login, list_users


def main():
    while True:
        print("\n--- User Manager ---")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Список пользователей")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            username = input("Имя пользователя: ")
            password = input("Пароль: ")
            register(username, password)

        elif choice == "2":
            username = input("Имя пользователя: ")
            password = input("Пароль: ")
            login(username, password)

        elif choice == "3":
            list_users()

        elif choice == "0":
            print("👋 Пока!")
            break

        else:
            print("❌ Неверный ввод")


if __name__ == "__main__":
    main()
