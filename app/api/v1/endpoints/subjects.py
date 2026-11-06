from fastapi import APIRouter, HTTPException, status
from app.api.deps import SessionDep
from app.schemas.subject import SubjectCreate, SubjectRead, SubjectUpdate
from app.services.subject_service import subject_service

router = APIRouter()


@router.get("/", response_model=list[SubjectRead])
async def list_subjects(db: SessionDep, skip: int = 0, limit: int = 100):
    return await subject_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=SubjectRead, status_code=status.HTTP_201_CREATED)
async def create_subject(db: SessionDep, subject_in: SubjectCreate):
    return await subject_service.create(db, obj_in=subject_in)


@router.get("/{subject_id}", response_model=SubjectRead)
async def get_subject(db: SessionDep, subject_id: int):
    subject = await subject_service.get(db, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return subject


@router.put("/{subject_id}", response_model=SubjectRead)
async def update_subject(db: SessionDep, subject_id: int, subject_in: SubjectUpdate):
    subject = await subject_service.get(db, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return await subject_service.update(db, db_obj=subject, obj_in=subject_in)

