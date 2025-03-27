from typing import List
from pydantic import BaseModel

class Task(BaseModel):
    name : str
    description : str

class TaskList(BaseModel):
    tasks : List[Task] = []