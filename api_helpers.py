import requests


BASE_URL = "https://jsonplaceholder.typicode.com"  # Or your actual base URL

def get_users():
    return requests.get(f"{BASE_URL}/users")

def get_user_by_id(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}").json()


def get_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    return response
