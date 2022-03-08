from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

class PostModel(BaseModel):
    title:str
    content:str
    published:bool=True

class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime
    class Config:
        orm_mode=True

class PostCreate(PostModel):
    pass

class Post(PostModel):
    id:int
    created_at:datetime
    user_id:int
    user:UserOut

    class Config:
        orm_mode=True
        column_default_sort=True
class PostVote(BaseModel):
    Post:Post
    votes:int
    class Config:
        orm_mode=True
        column_default_sort=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str





class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData():

    id: Optional[str]=None

class UserLogin(BaseModel):
    email:str
    password:str

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

