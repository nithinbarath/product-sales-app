from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.todolist import Todolist
from schemas.todolist import CreateTodolist, UpdateTodolist, DeleteTodolist




def create_list(session: Session, list:CreateTodolist):

    record = session.query(Todolist).filter(Todolist.notes == list.notes).first()

    if record:
        raise HTTPException(status_code=400, detail="Notes Already Created")
    else:
        db_todolist = Todolist(notes=list.notes)
        session.add(db_todolist)
        session.commit()
        session.refresh(db_todolist)
        return db_todolist

def get_todolist(session: Session):

    record = session.query(Todolist).all()

    return record

def update_todolist(session: Session, list:UpdateTodolist):

    record = session.query(Todolist).filter(Todolist.id==list.id).first()

    if record:
        record.notes = list.notes
        session.commit()
        session.refresh(record)
        return record
    else:
        raise HTTPException(status_code=402,detail='invalid value')

def delete_todolist(session: Session, list_id:DeleteTodolist):

    record = session.query(Todolist).filter(Todolist.id == list_id.id).first()

    if record:

        session.delete(record)
        session.commit()

        return 'deleted successfully'
    else:

         raise HTTPException(status_code=402,detail='invalid value')

