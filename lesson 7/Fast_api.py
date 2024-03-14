import string

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator

app = FastAPI()


class Task(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: str
    status: str

    @field_validator('status')
    @classmethod
    def check_status(cls, status):
        if status not in ["open", "close"]:
            raise ValueError('error')
        return status


tasks = []


@app.get("/")
async def getTasks():
    return tasks


@app.post("/")
async def add_task(task: Task):
    try:
        tasks.append(task.dict())
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@app.put("/")
async def update_task(task: Task):
    for index, existing_task in enumerate(tasks):
        if existing_task['id'] == task.id:
            try:
                tasks[index] = task.dict()
            except ValidationError:
                raise HTTPException(status_code=400, detail="oops... an error occurred")
            return f"Updated task with ID: {task.id}"
    raise HTTPException(status_code=404, detail=f"Task with ID {task.id} not found")


@app.delete("/{Id}")
async def delete_task(Id: int):
    for task in tasks:
        if task['id'] == Id:
            try:
                tasks.remove(task)
            except ValidationError:
                raise HTTPException(status_code=400, detail="oops... an error occurred")
            return f"Deleted task with ID: {Id}"


if __name__ == "__main__":
    uvicorn.run("Fast_api:app", host="127.0.0.1", port=8080, reload="true")
