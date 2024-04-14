from abc import ABC, abstractmethod
from typing import List
from pytest import Session
from app.modules.location.aplication.dto import CityResponseDTO, CountryResponseDTO
from app.seedwork.domain.repositories import Repository


class CountryRepository(Repository, ABC):

    @abstractmethod
    def get_all(self, db: Session) -> List[CountryResponseDTO]:
        pass


class CityRepository(Repository, ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int, db: Session) -> List[CityResponseDTO]:
        pass

    @abstractmethod
    def get_all(self, db: Session) -> List[CityResponseDTO]:
        pass
