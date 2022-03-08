from tkinter import CASCADE
from sqlalchemy.sql.expression  import  func
from sqlite3 import Timestamp
from .database import Base
from sqlalchemy import DATETIME, TIMESTAMP, VARCHAR, Boolean, Column, ForeignKey,Integer, String, false
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="posts"


    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='True',nullable=False)
    created_at=Column(DATETIME(timezone=True),nullable=False,server_default=func.now() )
    user_id=Column(Integer,ForeignKey("users.id",ondelete=CASCADE), nullable=False)

    user= relationship("User")
   

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(VARCHAR(50),nullable=False,unique=True)  
    password=Column(String,nullable=False)
    created_at=Column(DATETIME(timezone=True),nullable=False,server_default=func.now())

class Vote(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete=CASCADE),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete=CASCADE),primary_key=True)

