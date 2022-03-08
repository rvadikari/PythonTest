from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import status,APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,utils,oauth2


router=APIRouter(tags=['Auth'])

@router.get("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    
   
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
 
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    if not utils.Verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    access_token=oauth2.Create_Access_Token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}


