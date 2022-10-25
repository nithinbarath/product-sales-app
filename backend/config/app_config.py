# in-built
import traceback
from os import environ
from os.path import dirname, join
from sys import exit

# 3rd party
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_jwt_auth import AuthJWT
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# custom
from config.auth_config import AuthSettings
from crud.signup import is_token_disabled
# from config.log_config import logger, json_logging
# from processing.authentication.admin_events import \
#     AuthenticationEvents as auth_events

try:
    # CORS
    origins = [
        "http://localhost:3000",
        "*"
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


    # Fast API app
    app = FastAPI(middleware=middleware)


    @AuthJWT.load_config
    def get_config():
        return AuthSettings()

    
    @AuthJWT.token_in_denylist_loader
    def check_if_token_in_denylist(decrypted_token) -> bool:
        jti = decrypted_token['jti']
        result = is_token_disabled(token=jti)
        return result.is_success


except Exception as e:
    # logger.error(e)
    # logger.error(traceback.format_exc())
    exit(1)
