from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .city_repository import CityRepositoryPostgres
from .country_repository import CountryRepositoryPostgres
from .exceptions import ImplementationNotExistForFabricTypeException
from ..domain.repository import CityRepository, CountryRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj_type) -> Repository:
        if obj_type == CityRepository:
            return CityRepositoryPostgres()
        if obj_type == CountryRepository:
            return CountryRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
