# User Manager

Educational backend project written in Python for managing users and roles.  
The project exposes a small API built with FastAPI and stores data in PostgreSQL.

## Technologies
- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Git

## Features

- user registration and login
- roles: `user / moderator / admin`
- password hashing
- list users (based on role)
- change user roles (admin only)
- audit log

## Quick Start

### 1) Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2) Configure PostgreSQL

Create a database named `user_manager`.

You can configure connection in two ways.

#### Option A: Environment variables (Windows PowerShell)

```powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="user_manager"
$env:PGUSER="postgres"
$env:PGPASSWORD="<your_postgres_password>"
```

#### Option B: Using .env (recommended)

1) Copy `.env.example` to `.env`  
2) Fill in your own values (password should not be pushed to GitHub)

### 3) Create database tables

```bash
python init_db.py
```

### 4) Run the API

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

http://127.0.0.1:8000/docs

## Authorization

Protected endpoints require headers:

- `X-Auth-Username`
- `X-Auth-Password`

## Endpoints

- `POST /register`
- `POST /login`
- `GET /users` (admin/moderator)
- `PATCH /users/{id}/role` (admin)

## Example Requests

### Register

```bash
curl -X POST "http://127.0.0.1:8000/register" ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"test\", \"password\": \"1234\"}"
```

### List users

```bash
curl -X GET "http://127.0.0.1:8000/users" ^
  -H "X-Auth-Username: admin" ^
  -H "X-Auth-Password: 1234"
```

### Change role

```bash
curl -X PATCH "http://127.0.0.1:8000/users/2/role" ^
  -H "Content-Type: application/json" ^
  -H "X-Auth-Username: admin" ^
  -H "X-Auth-Password: 1234" ^
  -d "{\"role\": \"moderator\"}"
```

---

# User Manager

Учебный backend-проект на Python: управление пользователями, роли и небольшой API на FastAPI.  
Хранение данных — PostgreSQL.

## Технологии
- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn
- Git

## Что есть в проекте

- регистрация и вход
- роли: `user / moderator / admin`
- хеширование паролей
- просмотр пользователей (по роли)
- смена ролей (только admin)
- audit log

## Быстрый старт

### 1) Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

### 2) Настройка PostgreSQL

Создай базу данных `user_manager`.

Дальше есть два варианта:

#### Вариант A: через переменные окружения (Windows PowerShell)

```powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="user_manager"
$env:PGUSER="postgres"
$env:PGPASSWORD="<your_postgres_password>"
```

#### Вариант B: через .env (удобнее)

1) Скопируй файл `.env.example` в `.env`  
2) Впиши свои значения (пароль не пушится в GitHub)

### 3) Создание таблиц

```bash
python init_db.py
```

### 4) Запуск API (FastAPI)

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

- http://127.0.0.1:8000/docs

## Авторизация для защищённых эндпоинтов

Для защищённых запросов используются заголовки:

- `X-Auth-Username`
- `X-Auth-Password`

## Эндпоинты

- `POST /register`
- `POST /login`
- `GET /users` (admin/moderator)
- `PATCH /users/{id}/role` (admin)

## Примеры запросов

### Регистрация

```bash
curl -X POST "http://127.0.0.1:8000/register" ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"test\", \"password\": \"1234\"}"
```

### Список пользователей (нужны заголовки)

```bash
curl -X GET "http://127.0.0.1:8000/users" ^
  -H "X-Auth-Username: admin" ^
  -H "X-Auth-Password: 1234"
```

### Смена роли (admin)

```bash
curl -X PATCH "http://127.0.0.1:8000/users/2/role" ^
  -H "Content-Type: application/json" ^
  -H "X-Auth-Username: admin" ^
  -H "X-Auth-Password: 1234" ^
  -d "{\"role\": \"moderator\"}"
```

## Структура проекта

```text
user_manager/
  app/
    __init__.py
    main.py
    schemas.py
  audit_log.py
  db.py
  init_db.py
  main.py
  storage.py
  users.py
  schema.sql
  requirements.txt
  CHANGELOG.md
  README.md
  .gitignore
```

## Версии

История изменений — в `CHANGELOG.md`.
