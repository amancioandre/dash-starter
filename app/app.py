def create_app(env):
    try:
        from flask import Flask
        app = Flask(__name__)

        from app.config import config_by_env
        app.config.from_object(config_by_env[env])

        from app.database import db, init_db
        db.init_app(app)

        @app.before_first_request
        def create_user():
            init_db(db)

        from flask_migrate import Migrate
        migrate = Migrate()
        migrate.init_app(app)


        return app
    except BaseException as error:
        raise error