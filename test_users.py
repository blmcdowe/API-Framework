import pytest
from utils.api_helpers import get_users, get_user_by_id
from utils.validators import is_valid_email


def test_get_users_status_code():
    response = get_users()
    assert response.status_code == 200


def test_get_users_length():
    response = get_users()
    data = response.json()
    assert len(data) == 10


def test_user_fields():
    response = get_users()
    user = response.json()[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user


def test_all_user_emails_are_valid():
    response = get_users()
    users = response.json()
    for user in users:
        assert is_valid_email(user["email"]), f"Invalid email: {user['email']}"


def test_user_1_name_is_leanne_graham():
    user = get_user_by_id(1)
    assert user["name"] == "Leanne Graham"
