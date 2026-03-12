from fastapi import FastAPI
from sqlalchemy import text
from app.core.config import settings
from app.database import engine, SessionLocal, Base
from app.cache import get_redis
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app import models

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "User Manager API is running"}

@app.get("/health")
def health():
    db_status = "ok"
    redis_status = "ok"
    try:
        with SessionLocal() as db:
            db.execute(text("SELECT 1"))
    except Exception:
        db_status = "error"
    try:
        client = get_redis()
        if not client:
            redis_status = "disabled"
    except Exception:
        redis_status = "error"
    return {"status": "ok", "database": db_status, "redis": redis_status}
