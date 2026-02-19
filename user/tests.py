from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('user_create')

    data = {
        "name": "Pytest User",
        "username": "pytestuser",
        "password": "testpassword123",
        "role": "admin"   # yoki "user" — modelga qarab
    }

    response = api_client.post(url, data, format='json')

    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED



