from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    users,
    students,
    groups,
    subjects,
    attendances,
    grades,
    payments,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
api_router.include_router(users.router, prefix="/users", tags=["Usuarios"])
api_router.include_router(students.router, prefix="/students", tags=["Alumnos"])
api_router.include_router(groups.router, prefix="/groups", tags=["Grupos"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["Materias"])
api_router.include_router(attendances.router, prefix="/attendances", tags=["Asistencias"])
api_router.include_router(grades.router, prefix="/grades", tags=["Calificaciones"])
api_router.include_router(payments.router, prefix="/payments", tags=["Pagos"])

