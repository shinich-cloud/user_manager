# User Manager

Educational backend project for managing users and roles.  
The project provides an API built with FastAPI and stores data in PostgreSQL.

## Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Redis
- Docker
- Git

## Features

- user registration and login
- roles: `user / moderator / admin`
- password hashing
- JWT authorization
- list users with pagination
- search users by username
- change user roles (admin only)
- audit logs
- healthcheck endpoint
- Redis cache

## Quick Start

### 1) Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2) Configure PostgreSQL

Create a database named `user_manager`.

You can configure the connection in two ways.

#### Option A: Environment variables (Windows PowerShell)

```powershell
$env:DATABASE_URL="postgresql+psycopg2://postgres:<your_postgres_password>@localhost:5432/user_manager"
$env:JWT_SECRET_KEY="change_me_secret_key"
$env:REDIS_URL="redis://localhost:6379/0"
```

#### Option B: Using `.env` (recommended)

1. Copy `.env.example` to `.env`
2. Fill in your own values

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

Protected endpoints use Bearer token authentication.

### Login example

```bash
curl -X POST "http://127.0.0.1:8000/login" ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"admin\", \"password\": \"1234\"}"
```

After login use the token in:

```text
Authorization: Bearer <token>
```

## Endpoints

- `POST /register`
- `POST /login`
- `GET /users`
- `GET /users/me`
- `PATCH /users/{id}/role`
- `GET /users/logs`
- `GET /health`

## Project Structure

```text
user_manager/
  app/
    core/
      config.py
    routers/
      auth.py
      users.py
    __init__.py
    cache.py
    database.py
    deps.py
    main.py
    models.py
    schemas.py
    security.py
  .env.example
  .gitignore
  CHANGELOG.md
  docker-compose.yml
  Dockerfile
  init_db.py
  README.md
  requirements.txt
```

---

# Русская версия

# User Manager

Учебный backend-проект для управления пользователями и ролями.  
Проект предоставляет API на FastAPI и использует PostgreSQL для хранения данных.

## Технологии

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Redis
- Docker
- Git

## Возможности

- регистрация и вход пользователей
- роли: `user / moderator / admin`
- хеширование паролей
- JWT авторизация
- список пользователей с пагинацией
- поиск пользователей по имени
- изменение ролей (только admin)
- audit logs
- healthcheck endpoint
- Redis cache

## Быстрый старт

### 1) Установить зависимости

```bash
python -m pip install -r requirements.txt
```

### 2) Настроить PostgreSQL

Создай базу данных `user_manager`.

Можно настроить подключение двумя способами.

#### Вариант A: переменные окружения (Windows PowerShell)

```powershell
$env:DATABASE_URL="postgresql+psycopg2://postgres:<your_postgres_password>@localhost:5432/user_manager"
$env:JWT_SECRET_KEY="change_me_secret_key"
$env:REDIS_URL="redis://localhost:6379/0"
```

#### Вариант B: через `.env` (рекомендуется)

1. Скопируй `.env.example` в `.env`
2. Заполни свои значения

### 3) Создать таблицы

```bash
python init_db.py
```

### 4) Запустить API

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

http://127.0.0.1:8000/docs

## Авторизация

Защищённые эндпоинты используют Bearer token.

### Пример логина

```bash
curl -X POST "http://127.0.0.1:8000/login" ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"admin\", \"password\": \"1234\"}"
```

После логина используй токен в заголовке:

```text
Authorization: Bearer <token>
```

## Эндпоинты

- `POST /register`
- `POST /login`
- `GET /users`
- `GET /users/me`
- `PATCH /users/{id}/role`
- `GET /users/logs`
- `GET /health`
