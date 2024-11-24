from abc import ABC, abstractclassmethod
from typing import Any

class UseCaseInterface(ABC):

    @abstractclassmethod
    def execute(self, input: Any) -> Any:
        raise NotImplementedError    
