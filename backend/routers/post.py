from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schema import post as post_schema
from cruds import auth as auth_cruds
from models import Article
from database import get_db

router = APIRouter(prefix="/post", tags=["post"])

DbDependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(auth_cruds.get_current_user)]


@router.post("/")
async def create_post(db: DbDependency, user: user_dependency, post_form: post_schema.PostRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated Failed")
    post_model = Article(**post_form.model_dump(), user_id=user.get("id"))
    
    db.add(post_model)
    db.commit()
    return {"msg": "success"}

@router.get("/own")
async def get_own_posts(db: DbDependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated Failed")
    posts = db.query(Article).filter(Article.user_id == user.get("id")).all()
    # print(len(posts))
    return posts