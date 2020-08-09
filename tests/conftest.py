import os

import pytest
from rest_framework.test import APIClient


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def client():
    return APIClient()
