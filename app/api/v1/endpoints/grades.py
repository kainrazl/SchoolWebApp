from fastapi import APIRouter, HTTPException, status
from app.api.deps import SessionDep
from app.schemas.grade import GradeCreate, GradeRead, GradeUpdate
from app.services.grade_service import grade_service

router = APIRouter()


@router.get("/", response_model=list[GradeRead])
async def list_grades(db: SessionDep, skip: int = 0, limit: int = 100):
    return await grade_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=GradeRead, status_code=status.HTTP_201_CREATED)
async def create_grade(db: SessionDep, grade_in: GradeCreate):
    return await grade_service.create(db, obj_in=grade_in)


@router.get("/{grade_id}", response_model=GradeRead)
async def get_grade(db: SessionDep, grade_id: int):
    grade = await grade_service.get(db, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    return grade


@router.put("/{grade_id}", response_model=GradeRead)
async def update_grade(db: SessionDep, grade_id: int, grade_in: GradeUpdate):
    grade = await grade_service.get(db, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    return await grade_service.update(db, db_obj=grade, obj_in=grade_in)

