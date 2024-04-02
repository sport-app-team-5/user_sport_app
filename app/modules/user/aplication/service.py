from typing import List
from sqlalchemy.orm import Session
from app.modules.user.aplication.dto import UserRequestDTO, UserResponseDTO
from app.modules.user.domain.repository import UserRepository
from app.modules.user.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Service


class UserService(Service):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    def create_user(self, user: UserRequestDTO, db: Session) -> UserResponseDTO:
        repository = self.repository_factory.create_object(UserRepository)
        return repository.create(user, db)

    def get_users(self, db: Session) -> List[UserResponseDTO]:
        repository = self.repository_factory.create_object(UserRepository)
        return repository.get_all(db)

    def get_user_by_id(self, user_id: int, db: Session) -> UserResponseDTO:
        repository = self.repository_factory.create_object(UserRepository)
        return repository.get_by_id(user_id, db)
