from datetime import date
from app.schemas.common import BaseSchema, TimestampSchema
from app.schemas.group import GroupRead


class StudentBase(BaseSchema):
    enrollment_number: str
    first_name: str
    last_name: str
    birth_date: date | None = None
    gender: str | None = None
    curp_or_dni: str | None = None
    is_active: bool = True
    group_id: int | None = None
    user_id: int | None = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseSchema):
    enrollment_number: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None
    gender: str | None = None
    curp_or_dni: str | None = None
    is_active: bool | None = None
    group_id: int | None = None
    user_id: int | None = None


class StudentRead(StudentBase, TimestampSchema):
    id: int
    group: GroupRead | None = None

