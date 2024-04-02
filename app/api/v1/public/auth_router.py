from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.moduls.auth.aplication.dto import TokenResponse
from app.moduls.auth.aplication.service import AuthService

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/login", response_model=TokenResponse)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    auth_service = AuthService()
    access_token = auth_service.authenticate_user(form_data, db)
    return access_token
