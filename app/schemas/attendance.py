import datetime
from app.models.attendance import AttendanceStatus
from app.schemas.common import BaseSchema, TimestampSchema


class AttendanceBase(BaseSchema):
    date: datetime.date
    status: AttendanceStatus = AttendanceStatus.PRESENT
    remarks: str | None = None
    student_id: int
    subject_id: int


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseSchema):
    date: datetime.date | None = None
    status: AttendanceStatus | None = None
    remarks: str | None = None
    student_id: int | None = None
    subject_id: int | None = None


class AttendanceRead(AttendanceBase, TimestampSchema):
    id: int

