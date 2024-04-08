from dataclasses import dataclass
from pydantic import ConfigDict, BaseModel


@dataclass(frozen=True)
class LocationResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    model_config = ConfigDict(from_attributes=True)


@dataclass(frozen=True)
class CountryResponseDTO(LocationResponseDTO):
    pass


@dataclass(frozen=True)
class CityResponseDTO(LocationResponseDTO):
    country_id: int
