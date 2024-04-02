from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from app.modules.user.aplication.dto import UserResponseDTO, UserRequestDTO
from app.seedwork.domain.repositories import Repository


class UserRepository(Repository, ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int, db: Session) -> UserResponseDTO:
        pass

    @abstractmethod
    def get_all(self, db: Session) -> List[UserResponseDTO]:
        pass

    @abstractmethod
    def create(self, entity: UserRequestDTO, db: Session) -> UserResponseDTO:
        pass
