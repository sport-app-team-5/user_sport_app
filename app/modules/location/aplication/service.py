from typing import List
from sqlalchemy.orm import Session
from app.modules.location.aplication.dto import CityResponseDTO, CountryResponseDTO
from app.modules.location.domain.repository import CityRepository, CountryRepository
from app.modules.location.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service


class LocationService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def get_countries(self, db: Session) -> List[CountryResponseDTO]:
        repository = self.repository_factory.create_object(CountryRepository)
        return  repository.get_all(db)

    def get_cities(self, db: Session) -> List[CityResponseDTO]:
        repository = self.repository_factory.create_object(CityRepository)
        cities = repository.get_all(db)
        return [CityResponseDTO(id=city.id, name=city.name, code=city.code, country_id=city.country_id)
                for city in cities]

    def get_cities_by_country_id(self, db: Session, country_id: int = None) -> List[CityResponseDTO]:
        repository = self.repository_factory.create_object(CityRepository)
        cities = repository.get_by_id(country_id, db)
        return [CityResponseDTO(id=city.id, name=city.name, code=city.code, country_id=city.country_id)
                for city in cities]
