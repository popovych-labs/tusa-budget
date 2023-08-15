from typing import Callable

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .. import crud

def create_routes(
        path_to_templates: str,
        fn_get_db_session: Callable
):
    endpoints = APIRouter()

    templates = Jinja2Templates(directory=path_to_templates)

    @endpoints.get("/login", response_class=HTMLResponse)
    async def get_login(request: Request):
        return templates.TemplateResponse(name="index.html", context={"request": request})
    
    
    
    @endpoints.get("/dashboard")
    async def get_dashboard(request: Request):
        return templates.TemplateResponse(name="dashboard.html", context={"request": request})
    
    return endpoints