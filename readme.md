# User Manager v3.0.0 (PostgreSQL)

User Manager — консольное приложение на Python для управления пользователями с ролевой моделью доступа и audit-log.

## Возможности
- Регистрация и авторизация пользователей
- Роли: user / moderator / admin
- Первый зарегистрированный пользователь автоматически становится admin
- Audit-log действий (audit_logs.json)
- Хранение пользователей в PostgreSQL

## Требования
- Python 3.10+
- PostgreSQL 13+
- psycopg2-binary

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Настройка подключения
Задай переменные окружения:

Windows PowerShell:
```powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="user_manager"
$env:PGUSER="postgres"
$env:PGPASSWORD="your_password"
```

## Инициализация БД
```bash
python init_db.py
```

## Запуск
```bash
python main.py
```
