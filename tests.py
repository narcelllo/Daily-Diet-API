import pytest
import requests
import random
import string

BASE_URL = 'http://127.0.0.1:5000'

def test_create_user():
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24)) #https://hub.asimov.academy/tutorial/string-aleatoria-de-letras-maiusculas-e-digitos-em-python/
    new_user_data = {
    "username": f"test1_{random_string}",
    "password": "admin",
    "role": "admin"
    }
    response = requests.post(f"{BASE_URL}/user", json=new_user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json and "id" in response_json
    new_user_data['id'] = response_json['id']
    return new_user_data

def test_login_user():
    user_data = test_create_user()
    response = requests.post(f"{BASE_URL}/login", json=user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" and "id" in response_json

def test_delete_user():
    user_data = test_create_user()
    user_id = user_data['id']
    response = requests.delete(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 200