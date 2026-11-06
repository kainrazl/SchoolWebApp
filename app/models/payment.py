from datetime import date
from decimal import Decimal
from enum import Enum
from sqlalchemy import Date, ForeignKey, Integer, Numeric, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"


class PaymentMethod(str, Enum):
    CASH = "cash"
    TRANSFER = "transfer"
    CARD = "card"


class Payment(Base, TimestampMixin):
    __tablename__ = "payment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    concept: Mapped[str] = mapped_column(String(150), nullable=False)  # Ej. "Inscripción", "Colegiatura Septiembre"
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    payment_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    status: Mapped[PaymentStatus] = mapped_column(
        SQLEnum(PaymentStatus, native_enum=False, length=20),
        default=PaymentStatus.PAID,
        nullable=False,
    )
    payment_method: Mapped[PaymentMethod] = mapped_column(
        SQLEnum(PaymentMethod, native_enum=False, length=20),
        default=PaymentMethod.CASH,
        nullable=False,
    )
    receipt_number: Mapped[str | None] = mapped_column(String(50), unique=True, nullable=True)  # Folio o recibo

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), nullable=False)
    student: Mapped["Student"] = relationship(back_populates="payment", lazy="selectin")

