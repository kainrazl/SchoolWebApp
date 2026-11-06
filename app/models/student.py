from datetime import date
from sqlalchemy import Boolean, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class Student(Base, TimestampMixin):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    enrollment_number: Mapped[str] = mapped_column(String(30), unique=True, index=True, nullable=False)  # Matrícula
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    gender: Mapped[str | None] = mapped_column(String(10), nullable=True)
    curp_or_dni: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relación con Usuario (opcional si el alumno tiene cuenta de acceso)
    user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("user.id"), nullable=True)
    user: Mapped["User | None"] = relationship(back_populates="student", lazy="selectin")

    # Relación con Grupo
    group_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("group.id"), nullable=True)
    group: Mapped["Group | None"] = relationship(back_populates="student", lazy="selectin")

    # Relaciones académicas y administrativas
    attendance: Mapped[list["Attendance"]] = relationship(back_populates="student")
    grade: Mapped[list["Grade"]] = relationship(back_populates="student")
    payment: Mapped[list["Payment"]] = relationship(back_populates="student")

