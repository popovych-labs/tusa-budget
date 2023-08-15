from typing import Callable, Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from .. import crud

def create_serurity_routes(fn_get_db_session: Callable):
    endpoints = APIRouter()

    @endpoints.post("/token")
    async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                    db: Session = Depends(fn_get_db_session)):
        username, password = form_data.username, form_data.password

        db_user = crud.get_user_by_username(db, username=username)

        if db_user is None:
            raise HTTPException(status_code=404, detail="Unknown user")

        if str(db_user.password) != password:
            raise HTTPException(status_code=40, detail="Incorrect password")
        
        return {"access_token": username, "token_type": "bearer"}

    return endpoints