import json
import os

import pytest

from apps.types.models import Type


TESTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def types_data():
    path = os.path.join(TESTS_DIR, "data/types.json")
    with open(path) as f:
        types_data = json.load(f)
        return types_data


@pytest.fixture
def create_type(types_data):
    data = types_data["type_valid"]

    return Type.objects.create(**data)