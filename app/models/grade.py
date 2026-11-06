from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class Grade(Base, TimestampMixin):
    __tablename__ = "grade"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    period: Mapped[str] = mapped_column(String(50), nullable=False)  # Ej. "1er Parcial", "Trimestre 1"
    score: Mapped[float] = mapped_column(Float, nullable=False)  # Ej. 8.5
    remarks: Mapped[str | None] = mapped_column(String(255), nullable=True)

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), nullable=False)
    student: Mapped["Student"] = relationship(back_populates="grade", lazy="selectin")

    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subject.id"), nullable=False)
    subject: Mapped["Subject"] = relationship(back_populates="grade", lazy="selectin")

