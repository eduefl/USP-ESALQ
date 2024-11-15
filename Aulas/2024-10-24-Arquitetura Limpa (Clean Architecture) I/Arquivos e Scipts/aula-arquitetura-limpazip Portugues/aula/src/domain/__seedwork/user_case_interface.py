from abc import ABC, abstractclassmethod
from typing import Any

class UseCaseInterface(ABC):

    @abstractclassmethod
    def execute(input: Any) -> Any:
        raise NotImplementedError    
