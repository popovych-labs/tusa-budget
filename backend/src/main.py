import os

from fastapi import FastAPI, Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import endpoints

from . import db_connections
from . import config


CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = CURRENT_FILE_DIR + "/dist"
TEMPLATES_DIR = CURRENT_FILE_DIR + "/templates"
JS_DIR = CURRENT_FILE_DIR + "/js"
STYLE_DIR = CURRENT_FILE_DIR + "/style"

def app_factory():
    app = FastAPI()

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

    templates = Jinja2Templates(directory=TEMPLATES_DIR)

    fn_get_db_session = db_connections.get_db_session_factory(
        db_url=str(config.settings.db_url),
        connect_args=config.settings.db_connect_args,
    )

    router_app = endpoints.application.create_routes(
        index_dir=DIST_DIR,
        templates=templates,
        fn_get_db_session=fn_get_db_session,
        oauth2_scheme=oauth2_scheme
    )
    router_security = endpoints.security.create_serurity_routes(
        fn_get_db_session=fn_get_db_session,
    )
    app.include_router(router_app)
    app.include_router(router_security)

    app.mount("/", StaticFiles(directory=DIST_DIR, html = True), name="static")

    @app.exception_handler(405)
    async def error_handler(request: Request, exc: HTTPException):
        return templates.TemplateResponse(name="_404.html", context={"request": request})


    return app