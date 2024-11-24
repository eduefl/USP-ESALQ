from pydantic import BaseModel
from uuid import UUID
# INPUT

class UpdateUserInputDto(BaseModel):
    id: UUID
    name: str

# OUTPUT

class UpdateUseroUTPUTDto(BaseModel):
    id: UUID
    name: str