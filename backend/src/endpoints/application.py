from typing import Callable, Annotated

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .. import crud


def create_routes(
        path_to_templates: str,
        fn_get_db_session: Callable,
        oauth2_scheme: OAuth2PasswordBearer
):
    endpoints = APIRouter()

    templates = Jinja2Templates(directory=path_to_templates)

    def validate_token(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(fn_get_db_session)]):
        db_user = crud.get_user_by_username(db, username=token)

        if db_user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return token

    @endpoints.get("/{page_name}", response_class=HTMLResponse)
    async def get_basic_page(request: Request):
        return templates.TemplateResponse(name="index.html", context={"request": request})
    
    @endpoints.post("/login")
    async def get_login_part(request: Request):
        return templates.TemplateResponse(
            name="_login.html", 
            context={"request": request},
            )
    
    @endpoints.post("/dashboard")
    async def get_dashboard_part(request: Request, token: Annotated[str, Depends(validate_token)], db: Annotated[Session, Depends(fn_get_db_session)]):
        db_tusa_tables = crud.get_tusa_tables_by_username(db, username=token)


        return templates.TemplateResponse(
            name="_dashboard.html", 
            context={
                "request": request,
                "tables_names": [table.name for table in db_tusa_tables]
                },
            )
    
    @endpoints.post("/tusa")
    async def get_tusa_part(request: Request, token: Annotated[str, Depends(validate_token)]):
        return templates.TemplateResponse(
            name="_tusa.html", 
            context={"request": request},
            )

    
    return endpoints