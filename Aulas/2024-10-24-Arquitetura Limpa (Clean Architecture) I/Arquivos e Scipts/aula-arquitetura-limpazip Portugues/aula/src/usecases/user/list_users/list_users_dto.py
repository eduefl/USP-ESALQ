from pydantic import BaseModel
# from domain.user.user_entity import User
from typing import List
from uuid import UUID

# INPUT

class ListUsersInputDto(BaseModel):
    pass

# OUTPUT
class UserDto(BaseModel):
        id: UUID
        name: str

# OUTPUT
class ListUsersOutputDto(BaseModel):
    users: List[UserDto]
