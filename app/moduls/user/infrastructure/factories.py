from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .repository import UserRepositoryPostgres
from ..domain.repository import UserRepository
from .exceptions import ImplementationNotExistForFabricTypeException


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type) -> Repository:
        if obj == UserRepository.__class__:
            return UserRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
