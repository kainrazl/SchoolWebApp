from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate
from app.services.base import BaseService

subject_service = BaseService[Subject, SubjectCreate, SubjectUpdate](Subject)

