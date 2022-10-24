from fastapi import APIRouter
from endpoint import  todolist


api_router = APIRouter()


api_router.include_router(todolist.router)

