import pytest
from httpx import Response
from app.modules.auth.domain.entities import Role
from app.modules.user.domain.entities import User
from app.seedwork.domain.entities import Country, City
from app.seedwork.presentation.utils import encode_password


@pytest.fixture
def auth_seeders(db) -> None:
    db.add(Role(code="DEPO", name="Deportista"))
    db.add(Country(name="Colombia", code="CO"))
    db.add(City(name="Medellin", code="MDE", country_id=1))
    db.add(User(residence_city_id=1, birth_city_id=1, role_id=1, email="deportista@sport.app", password=encode_password("secret"),
                name='deportista', lastname="no profesional", document_type="CC", document_number="123456789"))
    db.commit()


@pytest.fixture
def user_data() -> dict:
    return {
        "username": "deportista@sport.app",
        "password": "secret"
    }


class TestAuthRouter:
    def test_login_successful(self, client, auth_seeders, user_data):
        _login = login(client, user_data)

        assert _login.status_code == 200
        assert "access_token" in _login.json()
        assert "token_type" in _login.json()

    def test_login_failed(self, client, user_data):
        user_data["password"] = "fail"
        _login = login(client, user_data)

        assert _login.status_code == 400
        assert "access_token" not in _login.json()
        assert _login.json() == {'detail': 'Incorrect username or password'}


def login(client, login_data) -> Response:
    response = client.post("/api/v1/login", data=login_data)
    return response
