import pytest
from httpx import Response
from app.modules.auth.domain.entities import Role
from app.seedwork.domain.entities import City, Country


@pytest.fixture
def location_seeders(db) -> None:
    db.add(Country(name="Colombia", code="CO"))
    db.add(City(name="Medellin", code="MDE", country_id=1))
    db.commit()

class TestLocationRouter:
    def test_get_cities(self, client, headers, location_seeders):
        response = get_cities(client, headers=headers)
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_cities_by_country_id(self, client, headers, location_seeders):
        response = get_cities_by_country_id(client, country_id=1, headers=headers)
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_countries(self, client, headers, location_seeders):
        response = get_countries(client,headers=headers)
        assert response.status_code == 200
        assert len(response.json()) > 0



def get_cities(client, headers) -> Response:
    cities = client.get("/api/v1/locations/cities", headers=headers)
    return cities


def get_cities_by_country_id(client, country_id, headers) -> Response:
    cities = client.get(f"/api/v1/locations/cities/{country_id}", headers=headers)
    return cities


def get_countries(client, headers) -> Response:
    countries = client.get("/api/v1/locations/countries", headers=headers)
    return countries
