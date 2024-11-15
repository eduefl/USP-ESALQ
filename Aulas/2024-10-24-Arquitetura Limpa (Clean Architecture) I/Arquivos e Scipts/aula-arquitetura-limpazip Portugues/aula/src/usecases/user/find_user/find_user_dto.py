from pydantic import BaseModel
from uuid import UUID

# Input
class FindUserInputDto(BaseModel):
    id: UUID


# output
class FindUserOutputDto(BaseModel):
    id: UUID
    name: str
