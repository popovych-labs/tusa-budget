from typing import Annotated

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

def create_routes(
        path_to_templates: str,
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
    async def post_login(request: Request):
        form_data = await request.form()
        username, password = form_data['username'], form_data['password']

        if username == "sasha":
            return JSONResponse({}, status_code=200)
        else:
            return JSONResponse({"error": "Unknown user"}, status_code=401)
    
    
    return endpoints