import traceback

from fastapi import status
from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.hash import pbkdf2_sha256


from schemas.signup import Signup as SignupSchema, Login as LoginSchema
from schemas.common.process_response import ProcessResponse

from models.signup import Signup as SignupModels, UsersBlacklistedTokens

from security.securityutils import encrypt_metadata,decrypt_metadata

from application import get_db_session







def create_new_user(session: Session, user:SignupSchema):

    record = session.query(SignupModels).filter(SignupModels.email == user.email).first()

    if record:
        raise HTTPException(status_code=409,detail="user already exists")
    else:
        hashed_password = pbkdf2_sha256.hash(user.password)

        db_new_user = SignupModels(
            username=user.username,
            email=user.email,
            password=hashed_password)

        session.add(db_new_user)
        session.commit()
        session.refresh(db_new_user)
        return db_new_user

def login_auth(session: Session, user:LoginSchema):

    record = session.query(SignupModels).filter(SignupModels.email == user.email).first()

    if record:

        return (user.id,user.email,user.password)
        
        # if(pbkdf2_sha256.verify(user.password, record.password)):

        #     email: str = user.get('email', None)
        #     auth_metadata = {'email': email, 'id': str(user.id)}
        #     encrypted_token = encrypt_metadata(metadata=auth_metadata)
        #     access_token = authorize.create_access_token(subject=encrypted_token)
        #     refresh_token = authorize.create_refresh_token(subject=encrypted_token)
        #     authorize.set_access_cookies(access_token)
        #     authorize.set_refresh_cookies(refresh_token)
            
        #     return 'login successfull'


@staticmethod
def is_token_disabled(token: str) -> ProcessResponse:
    try:
        session = next(get_db_session())
        tokens = session.query(UsersBlacklistedTokens).filter_by(
            token=token).all()
        if len(tokens) > 0:
            return ProcessResponse(
                is_success=True,
                response_data={
                    'status': 'Blocked',
                    'message': 'Re-authenticate to login'
                    },
                    code=status.HTTP_403_FORBIDDEN
                    )
        else:
            return ProcessResponse(
                is_success=False
                )
    except Exception as e:
            # logger.error(e)
            # logger.error(traceback.format_exc())
            return ProcessResponse(
                is_success=True,
                code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

