from typing import Any
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from app.config.db import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def __app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db() -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(__app: FastAPI, db: SessionTesting) -> Generator[TestClient, Any, None]:
    def __get_test_db():
        try:
            yield db
        finally:
            pass

    # noinspection PyUnresolvedReferences
    app.dependency_overrides.update({get_db: __get_test_db})

    with TestClient(__app) as client:
        yield client





import pytest
from httpx import Response
from app.modules.auth.domain.entities import Role
from app.modules.user.domain.entities import User
from app.seedwork.presentation.utils import encode_password


@pytest.fixture
def auth_seeders(db) -> None:
    db.add(Role(code="DEPO", name="Deportista"))
    db.add(User(email="deportista@sport.app", role_id=1, password=encode_password("secret"), name='deportista',
                lastname="no profesional", document_type="CC", document_number="123456789"))
    db.commit()


@pytest.fixture
def user_data() -> dict:
    return {
        "username": "deportista@sport.app",
        "password": "secret",
        "role_id": 1,
        "name": 'deportista',
        "lastname": "no profesional",
        "document_type": "CC",
        "document_number": "123456789"
    }


@pytest.fixture
def headers() -> dict:
    return {
        "api_access_key": "api_access_key",
        "api_secret_access_key": "api_secret_access_key"
    }


class TestAuthRouter:
    def test_login_successful(self, client, auth_seeders, user_data):
        _login = login(client, user_data)

        assert _login.status_code == 200
        assert "access_token" in _login.json()
        assert "token_type" in _login.json()

    def test_login_failed(self, client):
        _login = login(client, {"username": "john", "password": "secret"})

        assert _login.status_code == 400
        assert "access_token" not in _login.json()
        assert "detail" in _login.json()


def login(client, login_data) -> Response:
    response = client.post("/api/v1/login", data=login_data)
    return response
