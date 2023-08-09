import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .endpoints import create_routes

CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = CURRENT_FILE_DIR + "/templates"
JS_DIR = CURRENT_FILE_DIR + "/js"
STYLE_DIR = CURRENT_FILE_DIR + "/style"

def app_factory():
    app = FastAPI()

    endpoints = create_routes(path_to_templates=TEMPLATES_DIR)
    app.include_router(endpoints)

    app.mount("/js", StaticFiles(directory=JS_DIR), name="js")
    app.mount("/style", StaticFiles(directory=STYLE_DIR), name="style")

    return app