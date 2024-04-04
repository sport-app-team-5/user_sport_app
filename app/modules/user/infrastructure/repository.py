from typing import List
from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.modules.user.aplication.dto import UserResponseDTO, UserRequestDTO
from app.modules.user.domain.entities import User
from app.modules.user.domain.repository import UserRepository
from app.seedwork.presentation.utils import encode_password


class UserRepositoryPostgres(UserRepository):
    @staticmethod
    def __validate_exist_user(entity_id: int, db: Session) -> User:
        user = db.query(User).filter(User.id == entity_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return user

    @staticmethod
    def validates_duplicate_fields(user: UserRequestDTO, db: Session) -> None:
        existing_user = db.query(User).filter(
            or_(User.email == user.email, User.document_number == user.document_number)).first()
        if existing_user:
            if existing_user.email == user.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The email already exists')
            elif existing_user.document_number == user.document_number:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='The document number already exists')

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

    def create(self, entity: UserRequestDTO, db: Session) -> UserResponseDTO:
        try:
            self.validates_duplicate_fields(entity, db)
            user = User(**entity.model_dump())
            user.password = encode_password(entity.password)
            db.add(user)
            db.commit()
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
