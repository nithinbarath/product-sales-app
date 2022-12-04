import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth.exceptions import AuthJWTException
from application import Base
from .users import api_router as users_api_router

from config.app_config import app

logger = logging.getLogger(__name__)

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


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