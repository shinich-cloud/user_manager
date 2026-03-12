from datetime import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=4, max_length=100)

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class RoleUpdate(BaseModel):
    role: str

class UsersPage(BaseModel):
    total: int
    page: int
    limit: int
    items: list[UserOut]

class AuditLogOut(BaseModel):
    id: int
    username: str
    action: str
    target: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True

class HealthOut(BaseModel):
    status: str
    database: str
    redis: str
