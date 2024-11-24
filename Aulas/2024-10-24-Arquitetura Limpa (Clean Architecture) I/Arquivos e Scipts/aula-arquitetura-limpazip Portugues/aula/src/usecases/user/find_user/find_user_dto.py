from pydantic import BaseModel
from typing import List
from uuid import UUID

# Input
class FindUserInputDto(BaseModel):
    id: UUID

class TaskOutputDto(BaseModel):
    id: UUID
    title: str
    description: str
    completed: bool 

# output
class FindUserOutputDto(BaseModel):
    id: UUID
    name: str
    tasks: List[TaskOutputDto]
    pending_tasks: int
