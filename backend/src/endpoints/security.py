from typing import Callable

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from .. import crud

def create_serurity_routes(fn_get_db_session: Callable):
    endpoints = APIRouter()

    @endpoints.post("/token")
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

    return endpoints