from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from .repository import UserRepositoryPostgres
from .exceptions import ImplementationNotExistForFabricTypeException
from ..domain.repository import UserRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj_type) -> UserRepositoryPostgres:
        if obj_type == UserRepository:
            return UserRepositoryPostgres()
        else:
            raise ImplementationNotExistForFabricTypeException()
