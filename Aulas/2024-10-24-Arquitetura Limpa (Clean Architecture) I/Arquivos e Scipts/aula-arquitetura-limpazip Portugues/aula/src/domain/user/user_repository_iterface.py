from abc import ABC, abstractclassmethod
from domain.user.user_entity import User
from uuid import UUID 
from typing import List

# Metodo> -> INPUT -> OUTPUT

class UserRepositoryInterface(ABC):
    
    @abstractclassmethod
    def add_user(self, user: User) -> None:
        raise NotImplementedError
    
    @abstractclassmethod
    def find_user(self, user_id: UUID) -> User:
        raise NotImplementedError    
    
    @abstractclassmethod
    def update_user(self, user: User) -> None:
        raise NotImplementedError        
    
    @abstractclassmethod
    def list_users(self) -> List[User]:
        raise NotImplementedError            