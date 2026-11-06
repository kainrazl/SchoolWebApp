from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class Subject(Base, TimestampMixin):
    __tablename__ = "subject"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)  # Ej. "MAT-101"
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    credits: Mapped[int] = mapped_column(Integer, default=5)

    attendance: Mapped[list["Attendance"]] = relationship(back_populates="subject")
    grade: Mapped[list["Grade"]] = relationship(back_populates="subject")

