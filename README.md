# User Manager

Консольное приложение и API для управления пользователями (PostgreSQL).

## Запуск PostgreSQL версии
1) Установить зависимости:
```
python -m pip install -r requirements.txt
```

2) Создать базу `user_manager` в PostgreSQL.

3) Задать переменные окружения (PowerShell):
```
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="user_manager"
$env:PGUSER="postgres"
$env:PGPASSWORD="your_password"
```

4) Создать таблицу:
```
python init_db.py
```

## Запуск FastAPI
```
uvicorn app.main:app --reload
```

Swagger:
- http://127.0.0.1:8000/docs

## Авторизация для защищённых эндпоинтов
Используются заголовки:
- `X-Auth-Username`
- `X-Auth-Password`

Эндпоинты:
- `POST /register`
- `POST /login`
- `GET /users` (admin/moderator)
- `PATCH /users/{id}/role` (admin)
