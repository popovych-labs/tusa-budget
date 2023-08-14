import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import db_connections, endpoints
from . import config


CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = CURRENT_FILE_DIR + "/templates"
JS_DIR = CURRENT_FILE_DIR + "/js"
STYLE_DIR = CURRENT_FILE_DIR + "/style"

def app_factory():
    app = FastAPI()

    fn_get_db_session = db_connections.get_db_session_factory(
        db_url=str(config.settings.db_url),
        connect_args=config.settings.db_connect_args,
    )

    router = endpoints.create_routes(
        path_to_templates=TEMPLATES_DIR,
        fn_get_db_session=fn_get_db_session,
    )
    app.include_router(router)

    app.mount("/js", StaticFiles(directory=JS_DIR), name="js")
    app.mount("/style", StaticFiles(directory=STYLE_DIR), name="style")

    return app