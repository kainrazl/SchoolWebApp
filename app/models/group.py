from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class Group(Base, TimestampMixin):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)  # Ej. "1°A", "3°B"
    grade_level: Mapped[str] = mapped_column(String(50), nullable=False)  # Ej. "Primaria", "Secundaria", "1er Semestre"
    shift: Mapped[str] = mapped_column(String(20), default="Matutino")  # Matutino / Vespertino
    school_cycle: Mapped[str] = mapped_column(String(20), nullable=False)  # Ej. "2026-2027"

    student: Mapped[list["Student"]] = relationship(back_populates="group")

