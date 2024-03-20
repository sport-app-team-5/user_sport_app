from typing import List
from fastapi import APIRouter, Depends, Path, Security, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.moduls.auth.domain.enums.permission_enum import PermissionEnum
from app.moduls.auth.domain.service import AuthService
from app.moduls.user.aplication.dto import UserResponseDTO, UserRequestDTO
from app.moduls.user.aplication.service import UserService
from app.seedwork.presentation.jwt import oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
user_router = APIRouter(
    prefix='/users',
    tags=["user"],
    dependencies=[Depends(oauth2_scheme)]
)


@user_router.post("", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED,
                  dependencies=[Security(authorized, scopes=[PermissionEnum.CREATE_USER.code])])
async def create_user(user: UserRequestDTO, db: Session = Depends(get_db)):
    user_service = UserService()
    user_created = user_service.create_user(user, db)
    return user_created


@user_router.get("", response_model=List[UserResponseDTO],
                 dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])])
async def get_users(db: Session = Depends(get_db)):
    user_service = UserService()
    users = user_service.get_users(db)
    return users


@user_router.get("/{user_id}", response_model=UserResponseDTO,
                 dependencies=[Security(authorized, scopes=[PermissionEnum.READ_USER.code])])
async def get_user_by_id(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user_service = UserService()
    user = user_service.get_user_by_id(user_id, db)
    return user
