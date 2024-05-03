from typing import Annotated
from datetime import datetime, timedelta, timezone
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError


from schema.user import UserRegister
from models import User

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JST = timezone(timedelta(hours=9), "JST")
SECRET_KEY = '748b3c75448cbddffc3e231b9012d055b09f043320a11888fe84fb3684379b7b'
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def create_user(db:Session, user_create: UserRegister):
    new_user = User(**user_create.model_dump(exclude=["password"]) ,
                    password=bcrypt_context.hash(user_create.password))
    db.add(new_user)
    db.commit()
    return new_user

async def delete_user(db: Session, user_id: int):
    target = db.query(User).filter(User.id == user_id).first()
    if target is not None:
        db.delete(target)
        db.commit()
        return {"msg": "success"}
    else:
        raise HTTPException(status_code=404,detail="user not found")

async def authenticate_user(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(username: str, user_id: int, expire_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(tz=JST) + expire_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm="HS256")

# async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
async def get_current_user(request: Request):
    try:
        token = request.cookies.get("access_token")
        if token is None:
            raise HTTPException(status_code=401, detail="Not verify")
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms="HS256")
        username = payload.get("sub")
        user_id = payload.get("id")
        if user_id is None or username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user")
        return {"username": username, "id": user_id}
    except JWTError:
        print("JWTError")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user~")
                                

class UserForm:
    def __init__(self, request, user_form=None) -> None:
        self.request = request
        self.user_form = user_form
        self.username = None 
        self.password = None
        
    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
        if self.password is None and self.password is None:
            self.password = self.user_form.password
            self.username = self.user_form.username