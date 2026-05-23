from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validate_user_bad_age():
    payload = {
        'username': 'john',
        'age': 17,
        'email': 'john@example.com',
        'password': 'securepass'
    }
    r = client.post('/validate_user', json=payload)
    assert r.status_code == 422
    data = r.json()
    assert data['code'] == 422
    assert 'Validation Error' in data['message']

def test_validate_user_ok():
    payload = {
        'username': 'alice',
        'age': 25,
        'email': 'alice@example.com',
        'password': 'longpass12'
    }
    r = client.post('/validate_user', json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data['ok'] is True
