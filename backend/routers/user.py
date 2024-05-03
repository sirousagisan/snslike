from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, status, Response, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from schema import user as user_schema
from cruds import auth as auth_crud
from database import get_db


DbDependency = Annotated[Session, Depends(get_db)]


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=user_schema.UserResponce, status_code=status.HTTP_201_CREATED)
async def register(user_create: user_schema.UserRegister, db: DbDependency):
    res = await auth_crud.create_user(db=db, user_create=user_create)
    return res

@router.post("/login")
async def login(request: Request, db: DbDependency, response: Response, user_form: user_schema.UserLogin):
    try:
        form = auth_crud.UserForm(request=request, user_form=user_form)
        await form.create_oauth_form()
        varidate = await login_for_access_token(response=response, db=db, form_data=form)
        if not varidate:
            raise HTTPException(status_code=401, detail="Login Failed")
        return {"msg": "ok"}
    except HTTPException:
        raise HTTPException(status_code=401, detail="Login Failed")

@router.post("/delete", response_model=user_schema.SuccessMsg)
async def delete(db: DbDependency, id: int):
    res = await auth_crud.delete_user(db=db, user_id=id)
    return res

@router.post("/token")
async def login_for_access_token(response: Response,db: DbDependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await auth_crud.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        return False
    token = auth_crud.create_access_token(username=user.username, user_id=user.id, expire_delta=timedelta(minutes=30))
    response.set_cookie(key="access_token", value=token, samesite="none", httponly=True, secure=True)
    return True