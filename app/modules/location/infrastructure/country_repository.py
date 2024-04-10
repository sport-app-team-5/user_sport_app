from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.location.aplication.dto import CountryResponseDTO
from app.modules.location.domain.repository import CountryRepository
from app.seedwork.domain.entities import Country


class CountryRepositoryPostgres(CountryRepository):

    def get_all(self, db: Session) -> List[CountryResponseDTO]:
        try:
            countries = db.query(Country).all()
            return countries
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
