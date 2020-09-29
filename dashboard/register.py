import os
from dash import Dash

from dashboard.config import META_DESCRIPTION, META_VIEWPORT, EXTERNAL_STYLESHEETS
from dashboard.guards import local_auth_guard

def register(server, title, url_base_pathname, layout, view):
    try:
        dashboard = Dash(
            __name__,
            server=server,
            url_base_pathname=url_base_pathname,
            meta_tags=[META_VIEWPORT, META_DESCRIPTION],
            external_stylesheets=EXTERNAL_STYLESHEETS,
            assets_folder=os.path.abspath("static/assets")
        )

        with server.app_context():
            dashboard.title=title
            dashboard.layout=layout()
            view(dashboard)
            
        local_auth_guard(dashboard)
        server.logger.info(f"Dashboard for {title} successfully registered.")
    except BaseException as error:
        raise error