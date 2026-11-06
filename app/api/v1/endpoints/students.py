from fastapi import APIRouter, HTTPException, status
from app.api.deps import CurrentUserDep, SessionDep
from app.schemas.student import StudentCreate, StudentRead, StudentUpdate
from app.services.student_service import student_service

router = APIRouter()


@router.get("/", response_model=list[StudentRead])
async def list_students(db: SessionDep, skip: int = 0, limit: int = 100):
    """Listar alumnos registrados."""
    return await student_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
async def create_student(db: SessionDep, student_in: StudentCreate):
    """Registrar un nuevo alumno."""
    existing = await student_service.get_by_enrollment(db, student_in.enrollment_number)
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"La matrícula '{student_in.enrollment_number}' ya está registrada.",
        )
    return await student_service.create(db, obj_in=student_in)


@router.get("/{student_id}", response_model=StudentRead)
async def get_student(db: SessionDep, student_id: int):
    """Obtener detalle de un alumno por ID."""
    student = await student_service.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return student


@router.put("/{student_id}", response_model=StudentRead)
async def update_student(db: SessionDep, student_id: int, student_in: StudentUpdate):
    """Actualizar datos de un alumno."""
    student = await student_service.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return await student_service.update(db, db_obj=student, obj_in=student_in)


@router.delete("/{student_id}", response_model=StudentRead)
async def delete_student(db: SessionDep, student_id: int):
    """Eliminar un alumno."""
    student = await student_service.remove(db, id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return student

