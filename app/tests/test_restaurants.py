import pytest

from rest_framework.test import APIClient

client = APIClient(SERVER_NAME='localhost')

@pytest.mark.django_db
def test_create_restaurant():

    payload = dict(
        name='Burger King',
    )

    response = client.post("/api/restaurant/create/", payload)

    assert response.status_code == 201
