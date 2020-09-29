from flask_security import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text

from app.database import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __str__(self):
        return self.name