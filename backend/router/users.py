from fastapi import APIRouter
from endpoint import  signup


api_router = APIRouter()


api_router.include_router(signup.router)

