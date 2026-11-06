from app.schemas.common import BaseSchema, TimestampSchema


class GradeBase(BaseSchema):
    period: str
    score: float
    remarks: str | None = None
    student_id: int
    subject_id: int


class GradeCreate(GradeBase):
    pass


class GradeUpdate(BaseSchema):
    period: str | None = None
    score: float | None = None
    remarks: str | None = None
    student_id: int | None = None
    subject_id: int | None = None


class GradeRead(GradeBase, TimestampSchema):
    id: int

