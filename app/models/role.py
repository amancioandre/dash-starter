from flask_security import RoleMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text

from app.database import db
from .base import BaseModel

class Role(BaseModel, RoleMixin):
    __tablename__ = "roles"

    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name