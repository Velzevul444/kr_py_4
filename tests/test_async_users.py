import pytest
import asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from my_project.main import app as myapp
from faker import Faker

faker = Faker()

@pytest.mark.asyncio
async def test_create_get_delete_user_isolated():
    # ensure clean state
    from my_project import main as m
    m.db.clear()

    transport = ASGITransport(app=myapp)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        username = faker.user_name()
        age = faker.random_int(min=19, max=90)
        r = await ac.post('/users', json={'username': username, 'age': age})
        assert r.status_code == 201
        data = r.json()
        user_id = data['id']

        r2 = await ac.get(f'/users/{user_id}')
        assert r2.status_code == 200

        r3 = await ac.delete(f'/users/{user_id}')
        assert r3.status_code == 204

        r4 = await ac.get(f'/users/{user_id}')
        assert r4.status_code == 404
