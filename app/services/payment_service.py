from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate
from app.services.base import BaseService

payment_service = BaseService[Payment, PaymentCreate, PaymentUpdate](Payment)

