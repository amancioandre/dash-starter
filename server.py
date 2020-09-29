import os

from app import create_app
env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True)