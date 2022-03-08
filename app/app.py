from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .database import get_db
app= FastAPI()

@app.get("/")
def root(db:Session=Depends(get_db)):
    if db:
        return{"message":"Welcome to python and Connection established"}
   
    return {"message":"Welcome to python"}