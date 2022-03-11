from calendar import c
import json
import pytest
from fastapi.testclient import TestClient
from urllib import parse
from app.app import app 
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import Base,engine, get_db
from alembic import command
from app.oauth2 import Create_Access_Token
from app import models



password= parse.quote_plus(settings.database_password)
sqlalchemy_Database_URL = f'postgresql://{settings.database_username}:{password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_Test'
engine = create_engine(sqlalchemy_Database_URL)


TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    # command.upgrade("head")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def  override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    res=client.post("/users/",json={"email":"rajee@12345.com","password":"rajee@123"})
    res_login= res.json()
    res_login["password"]="rajee@123"
    
    assert res.status_code==201
    return res_login
@pytest.fixture
def token(test_user):
    token= Create_Access_Token({"user_id":test_user["id"]})
    return token

@pytest.fixture
def authorized_client(client,token):
    client.headers={
         **client.headers,
         "Authorization":f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(session,test_user):
    test_post_data=[{
        "title":"1st Post",
        "content":"1st post content",
        "user_id":test_user["id"]
    },
    {
        "title":"2nd Post",
        "content":"2nd post content",
        "user_id":test_user["id"]
    },
    {
        "title":"3rd Post",
        "content":"2nd post content",
        "user_id":test_user["id"]
    }]
    def create_post(post):
        
        return models.Post(** post)
    posts= list(map(create_post,test_post_data))

    session.add_all(posts)
    session.commit()
    return session.query(models.Post).all()
    
