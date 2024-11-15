from pydantic import BaseModel
from uuid import UUID

# Input
class AddUserInputDto(BaseModel):
    name: str


# output
class AddUserOutputDto(BaseModel):
    id: UUID
    name: str
