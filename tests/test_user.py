
from app import schemas
import pytest


def test_root(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json().get("message") == "Welcome to python and Connection established"


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "rajee@12345.com", "password": "rajee@123"})
    new_user = schemas.UserOut(** res.json())
    assert new_user.email == "rajee@12345.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.get(
        "/login", data={"username": test_user["email"], "password": test_user["password"]})
    assert res.status_code == 200


@pytest.mark.parametrize("username,password,status_code", [("rajee@12345.com", "rajee", 403),
                                                           ("wrong@123","rajee@123", 422),
                                                           (None,"rajee@123", 422),
                                                           ("rajee@12345.com", "rajee@123",200)])
def test_incorrect_login(test_user, client, username, password, status_code):
    res = client.get(
        "/login", data={"username": username, "password":password})
    assert res.status_code == status_code
    # assert res.json().get("detail") == "Invalid credentials"
