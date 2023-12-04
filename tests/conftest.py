import pytest
from faker import Faker
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def faker() -> Faker:
    return Faker()
