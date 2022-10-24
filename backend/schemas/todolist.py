from pydantic import BaseModel


class CreateTodolist(BaseModel):
    notes: str

class UpdateTodolist(BaseModel):
    id: int
    notes: str

class DeleteTodolist(BaseModel):
    id: int
    
