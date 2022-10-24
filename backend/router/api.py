import logging
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .todolist import api_router


logger = logging.getLogger(__name__)


app = FastAPI(title="backend")

origins= [
    'http://localhost:3000'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(api_router,prefix='/api',tags=["todolist"])