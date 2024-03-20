from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.moduls.user.aplication.dto import UserResponseDTO
from app.moduls.user.domain.entities import User
from app.moduls.user.domain.repository import UserRepository
from app.seedwork.presentation.utils import encode_password


class UserRepositoryPostgres(UserRepository):
    @staticmethod
    def __validate_exist_user(entity_id: int, db: Session) -> User:
        user = db.query(User).filter(User.id == entity_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return user

    def get_by_id(self, entity_id: int, db: Session) -> UserResponseDTO:
        try:
            user = self.__validate_exist_user(entity_id, db)
            return user
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_all(self, db: Session) -> List[UserResponseDTO]:
        try:
            users = db.query(User).all()
            return users
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def create(self, entity: User, db: Session) -> UserResponseDTO:
        try:
            user = User(**entity.model_dump())
            user.password = encode_password(entity.password)
            db.add(user)
            db.commit()
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update(self, entity_id: int, entity: User, db: Session) -> UserResponseDTO:
        raise NotImplementedError

    def delete(self, entity_id: int, db: Session) -> UserResponseDTO:
        raise NotImplementedError
