import datetime
from enum import Enum
from sqlalchemy import Date, ForeignKey, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class AttendanceStatus(str, Enum):
    PRESENT = "present"          # Presente
    ABSENT = "absent"            # Falta
    LATE = "late"                # Retardo
    JUSTIFIED = "justified"      # Justificado


class Attendance(Base, TimestampMixin):
    __tablename__ = "attendance"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False, index=True)
    status: Mapped[AttendanceStatus] = mapped_column(
        SQLEnum(AttendanceStatus, native_enum=False, length=20),
        default=AttendanceStatus.PRESENT,
        nullable=False,
    )
    remarks: Mapped[str | None] = mapped_column(String(255), nullable=True)

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), nullable=False)
    student: Mapped["Student"] = relationship(back_populates="attendance", lazy="selectin")

    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subject.id"), nullable=False)
    subject: Mapped["Subject"] = relationship(back_populates="attendance", lazy="selectin")

