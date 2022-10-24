from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = environ['DB_URI']
print(DATABASE_URL)
Base = declarative_base()
db_engine = create_engine(
    DATABASE_URL, connect_args={'connect_timeout': 10},
    pool_size=100, echo=False
)

db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

def get_db_session():
    db: Session = db_session()
    try:
        yield db
    finally:
        db.close()
