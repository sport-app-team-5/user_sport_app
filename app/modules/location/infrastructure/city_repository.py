from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.location.aplication.dto import CityResponseDTO
from app.modules.location.domain.repository import CityRepository
from app.seedwork.domain.entities import City



class CityRepositoryPostgres(CityRepository):

    @staticmethod
    def __validate_exist_city(entity_id: int, db: Session) -> List[CityResponseDTO]:
        cities = db.query(City).filter(City.country_id == entity_id).all()
        if not cities:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='City not found')

        return cities

    def get_by_id(self, entity_id: int, db: Session) -> List[CityResponseDTO]:
        try:
            cities = self.__validate_exist_city(entity_id, db)
            return cities
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_all(self, db: Session) -> List[CityResponseDTO]:
        try:
            cities = db.query(City).all()
            return cities
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
