from pydantic import EmailStr
from app.schemas.common import BaseSchema, TimestampSchema


# --- Roles ---
class RoleBase(BaseSchema):
    name: str
    description: str | None = None


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase, TimestampSchema):
    id: int


# --- Usuarios ---
class UserBase(BaseSchema):
    email: EmailStr
    username: str
    full_name: str
    is_active: bool = True
    role_id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseSchema):
    email: EmailStr | None = None
    username: str | None = None
    full_name: str | None = None
    is_active: bool | None = None
    role_id: int | None = None
    password: str | None = None


class UserRead(UserBase, TimestampSchema):
    id: int
    role: RoleRead | None = None


# --- Tokens / Auth ---
class Token(BaseSchema):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseSchema):
    sub: str | None = None

