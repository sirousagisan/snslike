from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel, Field

class PostRequest(BaseModel):
    title: Optional[str] = Field(default=None, examples=["sample"])
    body: str = Field(min_length=1, examples=["sample post"])
    # user_id: int

class PostResponce(BaseModel):
    id: int
    title: Optional[str]
    body: str
    created_at: datetime
    likes: Optional[Any]
    tags: Optional[Any]