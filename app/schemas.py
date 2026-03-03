from pydantic import BaseModel, Field

class RegisterIn(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=256)

class LoginIn(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=256)

class RoleUpdateIn(BaseModel):
    role: str = Field(min_length=1, max_length=20)

class UserOut(BaseModel):
    id: int
    username: str
    role: str

class LoginOut(BaseModel):
    id: int
    username: str
    role: str
