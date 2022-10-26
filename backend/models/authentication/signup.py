from application import Base
from sqlalchemy import Column , Integer , String, Boolean, DateTime, sql




class Signup(Base):

    __tablename__ = "signup"

    id = Column ( Integer , primary_key = True , index = True )
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class UsersBlacklistedTokens(Base):

    __tablename__ = "users_blacklisted_tokens"

    id = Column ( Integer , primary_key = True , index = True )
    token = Column(String, nullable=False)
    is_disabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=sql.func.now())
    

