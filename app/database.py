
from http import server
from lib2to3.pytree import Base
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib as url
from .config import settings
from urllib import parse 

# params=url.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + Server + ';DATABASE=' + Database + ';')
# engine=create_engine("mssql+pyodbc:///?odbc_connect=%s&trusted_connection=yes" % params)
# print(Database+" and "+ Server)

# sqlalchemy_Database_URL=f'mssql+pyodbc://{settings.database_hostname }/{settings.database_name}?trusted_connection=yes&driver={settings.database_driver}'
password= parse.quote_plus(settings.database_password)
sqlalchemy_Database_URL = f'postgresql://{settings.database_username}:{password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(sqlalchemy_Database_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()
