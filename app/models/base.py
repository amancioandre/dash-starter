from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from app.database import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)