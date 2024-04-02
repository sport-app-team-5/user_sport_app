from fastapi import APIRouter
from app.api.v1.public import auth_router
from app.api.v1.private import user_router, seeder_router

public_router = APIRouter(prefix="")
public_router.include_router(auth_router)

private_router = APIRouter(prefix="/auth")
private_router.include_router(user_router)
private_router.include_router(seeder_router)
