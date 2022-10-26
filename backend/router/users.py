from fastapi import APIRouter
from backend.endpoint.authentication import  signup


api_router = APIRouter()


api_router.include_router(signup.router)

