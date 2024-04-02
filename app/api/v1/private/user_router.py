from typing import List
from fastapi import APIRouter, Depends, Path, Security
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.enums.permission_enum import PermissionEnum
from app.modules.auth.domain.service import AuthService
from app.modules.user.aplication.dto import UserResponseDTO
from app.modules.user.aplication.service import UserService
from app.seedwork.presentation.jwt import oauth2_scheme

auth_service = AuthService()
authorized = auth_service.authorized
user_router = APIRouter(
    prefix='/users',
    tags=["Users"],
    dependencies=[Depends(oauth2_scheme)]
)


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
