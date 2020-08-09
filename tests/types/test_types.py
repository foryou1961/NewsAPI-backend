import pytest

from rest_framework.exceptions import ErrorDetail

from apps.types.models import Type


pytestmark = pytest.mark.django_db

ERRORS = {
        "type_with_long_title": {
            'title': [ErrorDetail(string='Ensure this field has no more than 50 characters.', code='max_length')]
        },
        "type_with_long_color": {
            'color': [ErrorDetail(string='Ensure this field has no more than 50 characters.', code='max_length')]
        },
        "type_with_empty_title": {
            'title': [ErrorDetail(string='This field is required.', code='required')]
        },
        "type_with_empty_color": {
            'color': [ErrorDetail(string='This field is required.', code='required')]
        },
    }

class TestTypesCreate:

    @pytest.mark.parametrize(
        "type",
        [
            "type_valid",
            "type_with_long_title",
            "type_with_long_color",
            "type_with_empty_title",
            "type_with_empty_color",
        ]
    )
    def test_types_create(self, client, types_data, type,):
        data = types_data[type]
        types_create_url = "/types/"
        response = client.post(types_create_url, data)

        if response.status_code == 201:
            for item in types_data[type]:
                assert response.data[item] == types_data[type][item]

        else:
            assert response.status_code == 400
            assert response.data == ERRORS[type]


class TestTypeGet:

    def test_types_get(self, client, types_data, create_type):
        assert len(Type.objects.all()) > 0
        id = Type.objects.all()[0].id
        types_get_url = f"/types/{id}/"
        response = client.get(types_get_url)

        assert response.status_code == 200
        for item in types_data["type_valid"]:
            assert response.data[item] == types_data["type_valid"][item]

    def test_types_get_not_exist(self, client, types_data):
        if len(Type.objects.all()):
            max_id = max([item.id for item in Type.objects.all()])
        else:
            max_id = 1
        types_get_url = f"/types/{max_id + 1}/"
        response = client.get(types_get_url)

        assert response.status_code == 404

    def test_types_get_list(self, client, types_data, create_type):
        types_get_url = "/types/"
        response = client.get(types_get_url)

        assert response.status_code == 200
        assert len(response.data) == 1
        for item in types_data["type_valid"]:
            assert response.data[0][item] == types_data["type_valid"][item]

class TestTypeDelete:

    def test_types_delete(self, client, types_data, create_type):
        assert len(Type.objects.all()) > 0
        id = Type.objects.all()[0].id
        types_delete_url = f"/types/{id}/"
        response = client.delete(types_delete_url)

        assert response.status_code == 204
        assert id not in [item.id for item in Type.objects.all()]

    def test_types_delete_not_exist(self, client, types_data):
        if len(Type.objects.all()):
            max_id = max([item.id for item in Type.objects.all()])
        else:
            max_id = 1
        types_delete_url = f"/types/{max_id + 1}/"
        response = client.delete(types_delete_url)

        assert response.status_code == 404

class TestTypesPatch:


    @pytest.mark.parametrize(
        "type",
        [
            "type_valid_update",
            "type_with_long_title",
            "type_with_long_color",
            "type_with_empty_title",
            "type_with_empty_color",
        ]
    )
    def test_types_patch(self, client, types_data, type, create_type):
        data = types_data[type]
        assert len(Type.objects.all()) > 0
        id = Type.objects.all()[0].id
        types_patch_url = f"/types/{id}/"
        response = client.patch(types_patch_url, data)

        if response.status_code == 200:
            for item in types_data[type]:
                assert response.data[item] == types_data[type][item]
        else:
            assert response.status_code == 400
            assert response.data == ERRORS[type]
