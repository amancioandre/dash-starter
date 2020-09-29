from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(database):
    from app.models import User, Role, RoleUser
    database.create_all()