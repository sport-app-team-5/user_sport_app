from typing import List
from fastapi import APIRouter, Depends, Path, Security
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.location.aplication.service import LocationService
from app.modules.location.aplication.dto import CityResponseDTO, CountryResponseDTO


auth_service = AuthService()
authorized = auth_service.authorized
location_router = APIRouter(
    prefix='/locations',
    tags=["Locations"]
)


@location_router.get("/cities", response_model=List[CityResponseDTO])
async def get_cities(db: Session = Depends(get_db)):
    location_service = LocationService()
    cities = location_service.get_cities(db)
    return cities

@location_router.get("/cities/{country_id}", response_model=List[CityResponseDTO])
async def get_cities_by_country_id(country_id: int = Path(ge=1), db: Session = Depends(get_db)):
    location_service = LocationService()
    cities = location_service.get_cities_by_country_id(db, country_id=country_id)
    return cities

@location_router.get("/countries", response_model=List[CountryResponseDTO])
async def get_countries(db: Session = Depends(get_db)):
    location_service = LocationService()
    countries = location_service.get_countries(db)
    return countries