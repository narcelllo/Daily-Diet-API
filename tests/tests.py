import pytest
import requests
import app

BASE_URL = 'http://127.0.0.1:5000'

user = []
diet = []
    
def test_create_user():
    new_user_data = {
        "username": "Marcello",
        "password": "admin"
    }
    response = requests.post(f"{BASE_URL}/user", json=new_user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    user.append(response_json['id'])
    return new_user_data

def test_login_user():
    user_data = {
        "username": "Marcello",
        "password": "admin"
    }
    response = requests.post(f"{BASE_URL}/login", json=user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    assert "token" in response_json  

def test_create_diet():
    user_data = {
        "username": "Marcello",
        "password": "admin"
    }

    login_response = requests.post(f"{BASE_URL}/login", json=user_data)
    login_json = login_response.json() 
    assert login_response.status_code == 200
    assert "message" in login_json
    assert "id" in login_json
    assert "token" in login_json  
    token = login_json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    new_diet_data = {
        "title": "first diet",
        "description": "first description",
        "consistent_diet": True
    }
    response = requests.post(f"{BASE_URL}/diet", json=new_diet_data, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    diet.append(response_json['id'])
