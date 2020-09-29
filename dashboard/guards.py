import os
from flask_security import login_required

def local_auth_guard(dashboard):
    for view_func in dashboard.server.view_functions:
        if view_func.startswith("/"):
            dashboard.server.view_functions[view_func] = login_required(dashboard.server.view_functions[view_func])