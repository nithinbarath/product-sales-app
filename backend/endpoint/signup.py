from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT

from application import get_db_session

from schemas.signup import Signup
from crud.signup import create_new_user, login_auth
from schemas.common.process_response import SimpleResponse, ProcessResponse
from schemas.common.utils import make_response

from passlib.hash import pbkdf2_sha256


from schemas.signup import RefreshTokenSchema
from crud.signup import disable_user_token

from security.securityutils import encrypt_metadata

from models.signup import Signup as SignupModels

router = APIRouter()


@router.get("/health")
async def status_check():
    return Response(status_code=200)


@router.post("/signup")
async def signup(
        user: Signup,
        db_session: Session = Depends(get_db_session),
):
   return create_new_user(session=db_session,user=user)


@router.post("/login")
async def login(
        authorize: AuthJWT = Depends(),
        form: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):


    record = db_session.query(SignupModels).filter(SignupModels.email == form.username).first()

    if record:

        if(pbkdf2_sha256.verify(form.password, record.password)):

                email: str = form.username
                auth_metadata = {'email':email, 'id': record.id}
                encrypted_token = encrypt_metadata(metadata=auth_metadata)
                access_token = authorize.create_access_token(subject=encrypted_token)
                refresh_token = authorize.create_refresh_token(subject=encrypted_token)
                authorize.set_access_cookies(access_token)
                authorize.set_refresh_cookies(refresh_token)

                return {'login successfull',record.id}

@router.get("/verify")
async def verify_login(authorize: AuthJWT = Depends()):
    """
        When called will verify if the caller is authenticated or not.
        If not authenticated, will raise 403.
    :param authorize: AuthJWT
    :return: FastApi Response Object
    """
    authorize.jwt_required()
    return Response(status_code=200)


@router.get("/refresh", response_model=RefreshTokenSchema)
async def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()
    user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=user)
    # Set the JWT and CSRF double submit cookies in the response
    authorize.set_access_cookies(new_access_token)
    return RefreshTokenSchema(access_token=new_access_token)

@router.get("/refresh-revoke", response_model=SimpleResponse)
async def logout_refresh_revoke(
        authorize: AuthJWT = Depends(),
        db_session: Session = Depends(get_db_session)
):
    """
    Because the JWT are stored in an httponly cookie, we need the server to
    revoke the refresh token to achieve clean logout.
    """
    authorize.jwt_refresh_token_required()
    # write your store & check logic here
    execution: ProcessResponse = disable_user_token(
        token=authorize.get_raw_jwt()['jti'],
        session=db_session,
    )
    success_response = SimpleResponse(message="Refresh token revoked")
    return make_response(execution=execution, response=success_response)


@router.get("/access-revoke")
async def logout_access_revoke(
        authorize: AuthJWT = Depends(),
        db_session: Session = Depends(get_db_session)
):
    authorize.jwt_required()
    # write your store & check logic here
    execution: ProcessResponse = disable_user_token(
        token=authorize.get_raw_jwt()['jti'],
        session=db_session,
    )
    success_response = Response(status_code=201)
    success_response.set_cookie(
        'access_token_cookie', "", max_age=0, secure=True, httponly=True,
        samesite="none"
    )
    success_response.set_cookie(
        'refresh_token_cookie', "", max_age=0, secure=True, httponly=True,
        samesite="none"
    )
    return success_response, execution.code
