from datetime import date
from decimal import Decimal
from app.models.payment import PaymentMethod, PaymentStatus
from app.schemas.common import BaseSchema, TimestampSchema


class PaymentBase(BaseSchema):
    concept: str
    amount: Decimal
    payment_date: date
    status: PaymentStatus = PaymentStatus.PAID
    payment_method: PaymentMethod = PaymentMethod.CASH
    receipt_number: str | None = None
    student_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseSchema):
    concept: str | None = None
    amount: Decimal | None = None
    payment_date: date | None = None
    status: PaymentStatus | None = None
    payment_method: PaymentMethod | None = None
    receipt_number: str | None = None
    student_id: int | None = None


class PaymentRead(PaymentBase, TimestampSchema):
    id: int

