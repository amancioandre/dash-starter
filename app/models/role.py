from flask_security import RoleMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text

from app.database import db

class Role(db.Model, RoleMixin):
    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name