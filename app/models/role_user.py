from flask_security import RoleMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text

from app.database import db

class RoleUser(db.Model, RoleMixin):
    __tablename__ = 'roles_users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))

    