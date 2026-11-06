from app.models.group import Group
from app.schemas.group import GroupCreate, GroupUpdate
from app.services.base import BaseService

group_service = BaseService[Group, GroupCreate, GroupUpdate](Group)

