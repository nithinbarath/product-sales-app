from sqlalchemy import Column , Integer , String
from application import Base



class Todolist(Base):

    __tablename__ = "todolist"

    id = Column ( Integer , primary_key = True , index = True )
    notes = Column(String)
    

