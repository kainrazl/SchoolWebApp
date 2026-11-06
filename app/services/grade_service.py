from app.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeUpdate
from app.services.base import BaseService

grade_service = BaseService[Grade, GradeCreate, GradeUpdate](Grade)

