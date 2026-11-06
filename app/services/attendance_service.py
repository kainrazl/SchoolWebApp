from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate
from app.services.base import BaseService

attendance_service = BaseService[Attendance, AttendanceCreate, AttendanceUpdate](Attendance)

