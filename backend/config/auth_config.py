from pydantic import BaseModel

AUTH_EXPIRY_MINS = 90 * 60
REFRESH_EXPIRY_DAYS = 2 * 60 * 60
PASSWORD_RESET_EXPIRE_HOURS = 8 * 60

SECRET_KEY = b'dzkNgG84vKuh3CvWTzgXKZItY9BhHnN9'


class AuthSettings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY.decode("utf-8")
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_samesite: str = 'none'
    authjwt_cookie_secure: bool = True
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}

    # expiry deltas
    authjwt_access_token_expires: int = AUTH_EXPIRY_MINS
    authjwt_refresh_token_expires: int = REFRESH_EXPIRY_DAYS