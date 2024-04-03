import pytest
from httpx import Response
from app.modules.auth.domain.entities import Role
from app.seedwork.domain.entities import City, Country


@pytest.fixture
def user_seeders(db) -> None:
    db.add(Role(code="DEPO", name="Deportista"))
    db.add(Country(name="Colombia", code="CO"))
    db.add(City(name="Medellin", code="MDE", country_id=1))
    db.commit()


@pytest.fixture
def user_data() -> dict:
    return {
        "city_id": 1,
        "role_id": 1,
        "password": "secret",
        "email": "deportista@sport.app",
        "name": 'deportista',
        "lastname": "no profesional",
        "document_type": "CC",
        "document_number": "123456789"
    }


class TestCreateUserRouter:
    def test_create_user(self, client, headers, user_seeders, user_data):
        user_created = create_user(client, user_data, headers)
        user_created_json = user_created.json()

        assert user_created.status_code == 201
        assert "id" in user_created_json
        assert user_data['name'] == user_created_json["name"]
        assert user_data['email'] == user_created_json["email"]
        assert user_data['role_id'] == user_created_json["role_id"]

    def test_create_user_with_invalid_data(self, client, headers, user_seeders, user_data):
        user_data_fail = user_data["role_id"] = "fail"
        response = create_user(client, user_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_user_with_invalid_email(self, client, headers, user_seeders, user_data):
        user_data_fail = user_data["email"] = "fail"
        response = create_user(client, user_data_fail, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json

    def test_create_user_with_null_data(self, client, headers):
        response = create_user(client, None, headers)
        response_json = response.json()

        assert response.status_code == 422
        assert "detail" in response_json
        assert "body" in response_json["detail"][0]["loc"]


class TestGetUserRouter:
    def test_get_user(self, client, headers, user_seeders, user_data):
        user_created = create_user(client, user_data, headers)
        user_created_json = user_created.json()
        user = get_user(client, user_created_json["id"], headers)

        assert user.status_code == 200
        assert "id" in user.json()
        assert user_data["email"] == user.json()["email"]

    def test_get_user_with_no_found_id(self, client, headers):
        user_id = 4
        response = get_user(client, user_id, headers)

        assert response.status_code == 404
        assert "detail" in response.json()

    def test_get_user_with_invalid_id(self, client, headers):
        user_id = -4
        response = get_user(client, user_id, headers)

        assert response.status_code == 422
        assert "detail" in response.json()


#
class TestGetUsersRouter:
    def test_get_users(self, client, headers, user_seeders, user_data):
        create_user(client, user_data, headers)
        user = get_users(client, headers)

        assert user.status_code == 200
        assert "id" in user.json()[0]

    def test_get_users_empty(self, client, headers, user_seeders, user_data):
        user = get_users(client, headers)

        assert user.status_code == 200
        assert [] == user.json()


def create_user(client, data, headers) -> Response:
    user_created = client.post("/api/v1/users", headers=headers, json=data)
    return user_created


def get_user(client, user_id, headers) -> Response:
    user = client.get(f"/api/v1/auth/users/{user_id}", headers=headers)
    return user


def get_users(client, headers) -> Response:
    users = client.get("/api/v1/auth/users", headers=headers)
    return users
