from fastapi import APIRouter, HTTPException, status
from app.api.deps import SessionDep
from app.schemas.payment import PaymentCreate, PaymentRead, PaymentUpdate
from app.services.payment_service import payment_service

router = APIRouter()


@router.get("/", response_model=list[PaymentRead])
async def list_payments(db: SessionDep, skip: int = 0, limit: int = 100):
    return await payment_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(db: SessionDep, payment_in: PaymentCreate):
    return await payment_service.create(db, obj_in=payment_in)


@router.get("/{payment_id}", response_model=PaymentRead)
async def get_payment(db: SessionDep, payment_id: int):
    payment = await payment_service.get(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return payment


@router.put("/{payment_id}", response_model=PaymentRead)
async def update_payment(db: SessionDep, payment_id: int, payment_in: PaymentUpdate):
    payment = await payment_service.get(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return await payment_service.update(db, db_obj=payment, obj_in=payment_in)

