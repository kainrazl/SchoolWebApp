from fastapi import APIRouter, HTTPException, status
from app.api.deps import SessionDep
from app.schemas.group import GroupCreate, GroupRead, GroupUpdate
from app.services.group_service import group_service

router = APIRouter()


@router.get("/", response_model=list[GroupRead])
async def list_groups(db: SessionDep, skip: int = 0, limit: int = 100):
    return await group_service.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=GroupRead, status_code=status.HTTP_201_CREATED)
async def create_group(db: SessionDep, group_in: GroupCreate):
    return await group_service.create(db, obj_in=group_in)


@router.get("/{group_id}", response_model=GroupRead)
async def get_group(db: SessionDep, group_id: int):
    group = await group_service.get(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return group


@router.put("/{group_id}", response_model=GroupRead)
async def update_group(db: SessionDep, group_id: int, group_in: GroupUpdate):
    group = await group_service.get(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return await group_service.update(db, db_obj=group, obj_in=group_in)

