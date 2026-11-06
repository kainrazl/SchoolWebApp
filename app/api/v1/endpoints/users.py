from fastapi import APIRouter, HTTPException, status
from app.api.deps import CurrentUserDep, SessionDep
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import user_service

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def read_user_me(current_user: CurrentUserDep):
    """Obtener datos del usuario actualmente autenticado."""
    return current_user


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(db: SessionDep, user_in: UserCreate):
    """Registrar un nuevo usuario."""
    user = await user_service.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="El correo ya se encuentra registrado.")
    user = await user_service.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso.")
    return await user_service.create_user(db, obj_in=user_in)


@router.get("/", response_model=list[UserRead])
async def read_users(db: SessionDep, skip: int = 0, limit: int = 100):
    """Listar usuarios."""
    return await user_service.get_multi(db, skip=skip, limit=limit)

