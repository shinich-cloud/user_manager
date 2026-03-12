from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.database import get_db
from app.models import User, AuditLog
from app.schemas import UserOut, UsersPage, RoleUpdate, AuditLogOut
from app.deps import get_current_user, require_roles
from app.cache import get_json, set_json, delete_key

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=UsersPage)
def list_users(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    username: str | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("admin", "moderator")),
):
    cache_key = f"users:{page}:{limit}:{username or ''}"
    cached = get_json(cache_key)
    if cached:
        return cached
    query = db.query(User)
    if username:
        query = query.filter(User.username.ilike(f"%{username}%"))
    total = query.count()
    items = query.order_by(User.id).offset((page - 1) * limit).limit(limit).all()
    result = {
        "total": total,
        "page": page,
        "limit": limit,
        "items": [UserOut.model_validate(item).model_dump(mode="json") for item in items],
    }
    set_json(cache_key, result, ex=30)
    return result

@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/{user_id}/role", response_model=UserOut)
def change_role(
    user_id: int,
    payload: RoleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("admin")),
):
    if payload.role not in {"user", "moderator", "admin"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid role")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.role = payload.role
    db.add(AuditLog(user_id=current_user.id, username=current_user.username, action="change_role", target=user.username))
    db.commit()
    db.refresh(user)
    delete_key("users:1:10:")
    return user

@router.get("/logs", response_model=list[AuditLogOut])
def get_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("admin")),
):
    logs = db.query(AuditLog).order_by(AuditLog.id.desc()).limit(50).all()
    return logs
