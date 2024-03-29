from fastapi import APIRouter,Response,status,HTTPException,Depends
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import engine,get_db


router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    hased_password=utils.Hash(user.password)
    user.password=hased_password
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
        user=db.query(models.User).filter(models.User.id==id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,message=f"User with id : {id} is not found")
        return user
