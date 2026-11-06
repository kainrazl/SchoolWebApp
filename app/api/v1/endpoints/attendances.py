from fastapi import APIRouter, HTTPException, status
from app.api.deps import SessionDep
from app.schemas.attendance import AttendanceCreate, AttendanceRead, AttendanceUpdate
from app.services.attendance_service import attendance_service

router = APIRouter()


@router.get("/", response_model=list[AttendanceRead])
async def list_attendances(db: SessionDep, skip: int = 0, limit: int = 100):
    return await attendance_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=AttendanceRead, status_code=status.HTTP_201_CREATED)
async def create_attendance(db: SessionDep, attendance_in: AttendanceCreate):
    return await attendance_service.create(db, obj_in=attendance_in)


@router.get("/{attendance_id}", response_model=AttendanceRead)
async def get_attendance(db: SessionDep, attendance_id: int):
    attendance = await attendance_service.get(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Registro de asistencia no encontrado")
    return attendance


@router.put("/{attendance_id}", response_model=AttendanceRead)
async def update_attendance(db: SessionDep, attendance_id: int, attendance_in: AttendanceUpdate):
    attendance = await attendance_service.get(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Registro de asistencia no encontrado")
    return await attendance_service.update(db, db_obj=attendance, obj_in=attendance_in)

