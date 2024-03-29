from datetime import datetime,timedelta
from . import schemas
from jose import JWTError,jwt
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import database,models
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
#  "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = settings.algorithm
# "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
# 30

def Create_Access_Token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt =jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def Verify_Access_Token(token:str,credentials_exception):

    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        
        id:str=payload.get("user_id")
        print(id)

        if id is None:
            raise credentials_exception
        schemas.TokenData.id =id
        token_data=schemas.TokenData()
         
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)) :
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    token_data= Verify_Access_Token(token,credentials_exception)
    user=db.query(models.User).filter(models.User.id==token_data.id).first()
   
    return user
