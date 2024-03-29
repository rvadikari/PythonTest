
from sqlalchemy.sql.expression  import  func
from sqlite3 import Timestamp
from .database import Base
from sqlalchemy import DATETIME, TIMESTAMP, VARCHAR, Boolean, Column, ForeignKey,Integer, String, false, text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="posts"


    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='True',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()') )
    user_id=Column(Integer,ForeignKey("users.id"), nullable=False)

    user= relationship("User")
   

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(VARCHAR(50),nullable=False,unique=True)  
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default= text('now()'))

class Vote(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),primary_key=True)

