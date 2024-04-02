from fastapi import APIRouter
from app.api.v1.public import auth_router, user_router as public_user_router
from app.api.v1.private import seeder_router, user_router as private_user_router

public_router = APIRouter(prefix="")
public_router.include_router(auth_router)
public_router.include_router(public_user_router)

private_router = APIRouter(prefix="/auth")
private_router.include_router(private_user_router)
private_router.include_router(seeder_router)
