from app.schemas.common import BaseSchema, TimestampSchema


class GroupBase(BaseSchema):
    name: str
    grade_level: str
    shift: str = "Matutino"
    school_cycle: str


class GroupCreate(GroupBase):
    pass


class GroupUpdate(BaseSchema):
    name: str | None = None
    grade_level: str | None = None
    shift: str | None = None
    school_cycle: str | None = None


class GroupRead(GroupBase, TimestampSchema):
    id: int

