from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserRegister(BaseModel):
    username: str = Field(min_length=4, max_length=24, examples=["user1"])
    password: str = Field(min_length=8, examples=["test1234"])
    email: EmailStr = Field(examples=["aaa@mail.com"])

class UserLogin(BaseModel):
    # email: EmailStr = Field(examples=["aaa@mail.com"])
    username: str
    password: str = Field(min_length=8, examples=["test1234"])

class UserResponce(BaseModel):
    username: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class SuccessMsg(BaseModel):
    msg: str