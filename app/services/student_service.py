from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate
from app.services.base import BaseService


class StudentService(BaseService[Student, StudentCreate, StudentUpdate]):
    async def get_by_enrollment(self, db: AsyncSession, enrollment_number: str) -> Student | None:
        result = await db.execute(select(Student).where(Student.enrollment_number == enrollment_number))
        return result.scalars().first()


student_service = StudentService(Student)

