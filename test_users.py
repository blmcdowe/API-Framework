# This code can be ran with Docker and pytest
#-------------------------------
import pytest
import json
from pathlib import Path
from utils.api_helpers import get_users, get_user_by_id
from utils.validators import is_valid_email
from pytest_html import extras

# -------------------------------
# Snapshot folder
# -------------------------------
SNAPSHOT_DIR = Path(__file__).parent / "snapshots"
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------
# Helper function to save snapshot and attach to HTML
# -------------------------------
def save_snapshot(name: str, data: dict, request):
    """
    Save JSON snapshot to file and attach it to HTML report.
    """
    snapshot_file = SNAPSHOT_DIR / f"{name}.json"
    with snapshot_file.open("w") as f:
        json.dump(data, f, indent=4)

    # Attach to HTML report
    if request.config.pluginmanager.hasplugin("html"):
        request.node.extra = getattr(request.node, "extra", [])
        request.node.extra.append(extras.json(data, name=name))


# -------------------------------
# Test Cases
# -------------------------------

def test_get_users_status_code(request):
    """
    # TC-01: Verify Users Endpoint Status Code
    # Description: Ensure that the /users endpoint responds with HTTP 200 OK.
    """
    response = get_users()
    save_snapshot("test_get_users_status_code", {
        "status_code": response.status_code,
        "url": str(response.url)
    }, request)
    assert response.status_code == 200


def test_get_users_length(request):
    """
    # TC-02: Verify Number of Users Returned
    # Description: Validate that the API returns exactly 10 user objects.
    """
    response = get_users()
    data = response.json()
    save_snapshot("test_get_users_length", {
        "length": len(data),
        "users_sample": data[:2]
    }, request)
    assert len(data) == 10


def test_user_fields(request):
    """
    # TC-03: Verify User Object Fields
    # Description: Ensure each user object contains mandatory fields: id, name, and email.
    """
    user = get_users().json()[0]
    save_snapshot("test_user_fields", user, request)
    assert "id" in user
    assert "name" in user
    assert "email" in user


def test_all_user_emails_are_valid(request):
    """
    # TC-04: Validate All User Emails
    # Description: Check that every user's email conforms to a valid email format.
    """
    users = get_users().json()
    invalid_emails = [u["email"] for u in users if not is_valid_email(u["email"])]
    save_snapshot("test_all_user_emails_are_valid", {
        "users": users,
        "invalid_emails": invalid_emails
    }, request)
    assert not invalid_emails, f"Invalid emails found: {invalid_emails}"


def test_user_1_name_is_leanne_graham(request):
    """
    # TC-05: Verify Specific User Name
    # Description: Confirm that the user with ID 1 has the name 'Leanne Graham'.
    """
    user = get_user_by_id(1)
    save_snapshot("test_user_1_name_is_leanne_graham", user, request)
    assert user["name"] == "Leanne Graham"
