from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def Hash(password:str):
    return pwd_context.hash(password)

def Verify(plain_password:str,hased_password:str):
    return pwd_context.verify(plain_password,hased_password)
