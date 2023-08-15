from typing import Callable

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import crud

def create_routes(
        path_to_templates: str,
        fn_get_db_session: Callable
):
    endpoints = APIRouter()

    endpoints.api_route

    @endpoints.get("/data")
    async def get_data():

        DATA = {
            "a": 100,
            "b": 200,
            "c": 300,
        }

        return JSONResponse(content=DATA)


    templates = Jinja2Templates(directory=path_to_templates)

    @endpoints.get("/login", response_class=HTMLResponse)
    async def get_login(request: Request):
        return templates.TemplateResponse(name="index.html", context={"request": request})
    
    @endpoints.post("/login")
    async def post_login(request: Request, db: Session = Depends(fn_get_db_session)):
        form_data = await request.form()
        username, password = str(form_data['username']), form_data['password']

        db_user = crud.get_user_by_username(db, username=username)

        if db_user is None:
            return JSONResponse({
                "status": "error",
                "message": "username not found"
            }, status_code=404)
        
        hashed_password = str(password) + "notreallyhashed"

        if str(db_user.password) == hashed_password:
            return JSONResponse({
                "status": "ok",
                "message": ""
            }, status_code=200)
        
        return JSONResponse({
                "status": "error",
                "message": "wrong password"
            }, status_code=401)
    
    @endpoints.get("/dashboard")
    async def get_dashboard(request: Request):
        return templates.TemplateResponse(name="dashboard.html", context={"request": request})
    
    return endpoints