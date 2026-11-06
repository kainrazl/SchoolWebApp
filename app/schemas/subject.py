from app.schemas.common import BaseSchema, TimestampSchema


class SubjectBase(BaseSchema):
    code: str
    name: str
    description: str | None = None
    credits: int = 5


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(BaseSchema):
    code: str | None = None
    name: str | None = None
    description: str | None = None
    credits: int | None = None


class SubjectRead(SubjectBase, TimestampSchema):
    id: int

