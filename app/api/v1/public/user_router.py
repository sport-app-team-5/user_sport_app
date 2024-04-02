from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.modules.auth.domain.service import AuthService
from app.modules.user.aplication.dto import UserResponseDTO, UserRequestDTO
from app.modules.user.aplication.service import UserService

auth_service = AuthService()
authorized = auth_service.authorized
user_router = APIRouter(
    prefix='/users',
    tags=["Users"]
)


@user_router.post("", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequestDTO, db: Session = Depends(get_db)):
    user_service = UserService()
    user_created = user_service.create_user(user, db)
    return user_created
