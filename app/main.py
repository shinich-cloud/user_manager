import hashlib
from fastapi import FastAPI, HTTPException, Header
from storage import get_all_users, get_user_by_username, insert_user, update_user_role
from audit_log import write_log
from .schemas import RegisterIn, LoginIn, RoleUpdateIn, UserOut, LoginOut

ROLES = ("user", "moderator", "admin")

app = FastAPI(title="User Manager", version="4.0.0")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def auth_user(x_auth_username: str | None, x_auth_password: str | None):
    if not x_auth_username or not x_auth_password:
        raise HTTPException(status_code=401, detail="Auth required")
    u = get_user_by_username(x_auth_username)
    if not u or u["password"] != hash_password(x_auth_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return u

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/register", response_model=UserOut)
def register(payload: RegisterIn):
    if get_user_by_username(payload.username):
        raise HTTPException(status_code=409, detail="User already exists")
    role = "admin" if len(get_all_users()) == 0 else "user"
    user = insert_user(payload.username, hash_password(payload.password), role)
    write_log(payload.username, "register")
    return {"id": user["id"], "username": user["username"], "role": user["role"]}

@app.post("/login", response_model=LoginOut)
def login(payload: LoginIn):
    u = get_user_by_username(payload.username)
    if not u or u["password"] != hash_password(payload.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    write_log(payload.username, "login")
    return {"id": u["id"], "username": u["username"], "role": u["role"]}

@app.get("/users", response_model=list[UserOut])
def users(x_auth_username: str | None = Header(default=None), x_auth_password: str | None = Header(default=None)):
    cu = auth_user(x_auth_username, x_auth_password)
    if cu["role"] not in ("admin", "moderator"):
        raise HTTPException(status_code=403, detail="Forbidden")
    return [{"id": u["id"], "username": u["username"], "role": u["role"]} for u in get_all_users()]

@app.patch("/users/{user_id}/role", response_model=UserOut)
def set_role(user_id: int, payload: RoleUpdateIn, x_auth_username: str | None = Header(default=None), x_auth_password: str | None = Header(default=None)):
    cu = auth_user(x_auth_username, x_auth_password)
    if cu["role"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    if payload.role not in ROLES:
        raise HTTPException(status_code=400, detail="Invalid role")
    updated = update_user_role(user_id, payload.role)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    write_log(cu["username"], "change_role", updated["username"])
    return {"id": updated["id"], "username": updated["username"], "role": updated["role"]}
