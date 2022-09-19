import pytest

from rest_framework.test import APIClient


client = APIClient(SERVER_NAME='localhost')

@pytest.mark.django_db
def test_register_user():
    payload = dict(
        email='test3@example.com',
        password='testpass123',
        restaurant='1'
    )

    response = client.post("/account/register/", payload)

    data = response.data

    assert data['email'] == payload['email']
