from sqlalchemy.dialects.postgresql import UUID

from app.database import db
from .base import BaseModel

class RoleUser(BaseModel):
    __tablename__ = 'roles_users'

    user_id = db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('users.id'))
    role_id = db.Column('role_id', UUID(as_uuid=True), db.ForeignKey('roles.id'))

    