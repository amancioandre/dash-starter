from flask_security import UserMixin

from app.database import db
from .base import BaseModel

class User(BaseModel, UserMixin):
    __tablename__ = "users"

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __str__(self):
        return self.name