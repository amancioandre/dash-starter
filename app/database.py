from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(database):
    # Import models here
    database.create_all()