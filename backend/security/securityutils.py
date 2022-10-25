
import jwt
from cryptography.fernet import Fernet

from config.auth_config import SECRET_KEY


def encrypt_metadata(metadata: dict):
        try:
            fernet = Fernet(SECRET_KEY)
            encoded_token = jwt.encode(
                payload=metadata, key=SECRET_KEY, algorithm="HS256"
            )
            return fernet.encrypt(encoded_token).decode("utf-8")
        except Exception as e:

            raise ValueError("cannot encrypt metadata")


def decrypt_metadata(token: str):
        try:
            fernet = Fernet(SECRET_KEY)
            jwt_token = fernet.decrypt(token.encode())
            return jwt.decode(jwt_token, SECRET_KEY)

        except Exception as e:
           
            raise ValueError("cannot decrypt metadata")