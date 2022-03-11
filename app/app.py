from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .database import get_db
from fastapi.middleware.cors import CORSMiddleware
from .routers import post,user,auth,vote

app= FastAPI()


origins = [
    'https://www.google.com'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root(db:Session=Depends(get_db)):
    if db:
        return{"message":"Welcome to python and Connection established with github action CI/CD pipeline"}
   
    return {"message":"Welcome to python"}