from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, AuditLog
from app.schemas import UserCreate, UserLogin, Token, UserOut
from app.security import hash_password, verify_password, create_access_token

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == payload.username).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    users_count = db.query(User).count()
    role = "admin" if users_count == 0 else "user"
    user = User(username=payload.username, password_hash=hash_password(payload.password), role=role)
    db.add(user)
    db.flush()
    db.add(AuditLog(user_id=user.id, username=user.username, action="register", target=None))
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == payload.username).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    db.add(AuditLog(user_id=user.id, username=user.username, action="login", target=None))
    db.commit()
    token = create_access_token({"sub": user.username, "role": user.role})
    return Token(access_token=token)
