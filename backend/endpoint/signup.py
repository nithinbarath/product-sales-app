from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT

from application import get_db_session

from schemas.signup import Signup
from crud.signup import create_new_user, login_auth

from passlib.hash import pbkdf2_sha256


from schemas.signup import Signup as SignupSchema, Login as LoginSchema, RefreshTokenSchema

from security.securityutils import encrypt_metadata

from models.signup import Signup as SignupModels

router = APIRouter()


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


@router.get("/refresh", response_model=RefreshTokenSchema)
async def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()
    user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=user)
    # Set the JWT and CSRF double submit cookies in the response
    authorize.set_access_cookies(new_access_token)
    return RefreshTokenSchema(access_token=new_access_token)
