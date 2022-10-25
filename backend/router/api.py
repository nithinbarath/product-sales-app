import logging
from fastapi import  FastAPI
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from .users import api_router as users_api_router

from config.app_config import app

logger = logging.getLogger(__name__)




origins= [
    'http://localhost:3000'
]


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
        )
    ]

# app = FastAPI(title="backend",middleware=middleware)


app.include_router(users_api_router,prefix='/api',tags=["users"])