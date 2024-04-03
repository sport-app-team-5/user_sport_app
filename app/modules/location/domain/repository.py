from abc import ABC, abstractmethod

from app.seedwork.domain.repositories import Repository


class CountryRepository(Repository, ABC):
    ...

class CityRepository(Repository, ABC):
    ...