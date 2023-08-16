import os

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles

from . import endpoints

from . import db_connections
from . import config


CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = CURRENT_FILE_DIR + "/templates"
JS_DIR = CURRENT_FILE_DIR + "/js"
STYLE_DIR = CURRENT_FILE_DIR + "/style"

def app_factory():
    app = FastAPI()

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

    fn_get_db_session = db_connections.get_db_session_factory(
        db_url=str(config.settings.db_url),
        connect_args=config.settings.db_connect_args,
    )

    router_app = endpoints.application.create_routes(
        path_to_templates=TEMPLATES_DIR,
        fn_get_db_session=fn_get_db_session,
        oauth2_scheme=oauth2_scheme
    )
    router_security = endpoints.security.create_serurity_routes(
        fn_get_db_session=fn_get_db_session,
    )
    app.include_router(router_app)
    app.include_router(router_security)

    app.mount("/js", StaticFiles(directory=JS_DIR), name="js")
    app.mount("/style", StaticFiles(directory=STYLE_DIR), name="style")

    return app