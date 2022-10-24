from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends

from application import get_db_session
from schemas.todolist import CreateTodolist, UpdateTodolist, DeleteTodolist
from crud.todolist import create_list, get_todolist, update_todolist, delete_todolist

router = APIRouter()


@router.post("/create/todolist")
def create_todolist(list:CreateTodolist, sessipn: Session = Depends(get_db_session)):

    return create_list(session=sessipn,list=list)

@router.get("/list/todolist")
def list_todolist(session: Session = Depends(get_db_session)):

    return get_todolist(session=session)

@router.put("/update/todolist")
def update_list(list: UpdateTodolist, session: Session = Depends(get_db_session)):
    
    return update_todolist(session=session,list=list)

@router.delete('/delete/todolist')
def delete_list(list:DeleteTodolist, session: Session = Depends(get_db_session)):

    return delete_todolist(session=session, list_id=list)
