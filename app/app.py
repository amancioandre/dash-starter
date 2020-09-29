def create_app(env):
    try:
        from flask import Flask
        app = Flask(__name__)

        from app.config import config_by_env
        app.config.from_object(config_by_env[env])

        from app.database import db, init_db
        db.init_app(app)

        from flask_security import SQLAlchemyUserDatastore, Security, url_for_security, LoginForm
        from app.models import User, Role
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security = Security(app, user_datastore)

        @app.before_first_request
        def create_user():
            init_db(db)
            if not user_datastore.get_user("admin@admin.com"):
                user_datastore.create_role(name="admin", description="Admin")
                user_datastore.create_user(email="admin@admin.com", password="admin")
                db.session.commit()
                user_datastore.add_role_to_user("admin@admin.com", "admin")
                db.session.commit()

        @app.context_processor
        def login_context():
            return {
                "url_for_security": url_for_security,
                "login_user_form": LoginForm()
            }

        from flask_migrate import Migrate
        migrate = Migrate()
        migrate.init_app(app)

        from dashboard.router import init_router
        init_router(app)

        return app
    except BaseException as error:
        raise error