
from fastapi import FastAPI
from pydantic import BaseModel
from Models import Todo
    
app = FastAPI()

todos = []

@app.get("/todos")
async def get_todos():
    return {'todos': todos}

@app.get("/todos/{id}")
async def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    return {'message': 'No todos found'}


@app.post("/todo")
async def create_todo(todo: Todo):
    todos.append(todo)
    return "todo has been added"

@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
    return {'message': 'todo deleted'}

@app.put("/todos/{id}")
async def update_todo(todo: Todo):
    for item in todos:
        if item.id == todo.id:
            item.title = todo.title
    return {'message': f'todo {todo.id} updated'}


