## v4 - FastAPI version

### Added
- REST API на FastAPI
- эндпоинты для регистрации и входа
- Pydantic схемы
- запуск через Uvicorn

### Changed
- структура проекта (добавлена папка app)
- логика работы с пользователями перенесена в API

---

## v3 - PostgreSQL version

### Added
- подключение PostgreSQL
- файл db.py для работы с базой данных
- schema.sql для создания таблиц
- init_db.py для инициализации базы

### Changed
- хранение пользователей перенесено из JSON в PostgreSQL

---

## v2 - Roles system

### Added
- роли пользователей:
  - user
  - moderator
  - admin
- разграничение прав
- audit log

---

## v1 - Initial version

### Added
- регистрация пользователей
- вход в систему
- хранение пользователей в JSON