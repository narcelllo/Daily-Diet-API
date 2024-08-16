import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

user = []

def test_login_user():
    new_user_data = {
        "username": "Marcello",
        "password": "admin"
    }
    response = requests.post(f"{BASE_URL}/login", json=new_user_data)

    assert response.status_code == 200
    response_json = response.json()
    assert "message" and "id" in response_json
