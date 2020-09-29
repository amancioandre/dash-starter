from dashboard import register
from dashboard.pages.home import layout as home_layout, view as home_view

def init_router(server):
    with server.app_context():
        register(server, "home", "/", layout_home, view_home)