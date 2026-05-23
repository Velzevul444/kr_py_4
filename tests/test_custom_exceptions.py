from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_raise_a():
    r = client.get('/raise_a')
    assert r.status_code == 422
    data = r.json()
    assert data['code'] == 422
    assert 'Something went wrong A' in data['message']

def test_raise_b():
    r = client.get('/raise_b')
    assert r.status_code == 404
    data = r.json()
    assert data['code'] == 404
    assert 'Not found B' in data['message']
