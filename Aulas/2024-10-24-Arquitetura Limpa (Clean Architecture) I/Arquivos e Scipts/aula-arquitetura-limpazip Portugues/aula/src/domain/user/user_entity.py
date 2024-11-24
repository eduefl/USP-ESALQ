from uuid import UUID, uuid4
from typing import List
from domain.task.task_entity import Task
class User:

    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self, id: UUID, name: str ):
        self.id = id
        self.name = name
        self.tasks =[]
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
                raise Exception('id must be an UUID')
        if not isinstance(self.name, str) or len(self.name) ==0:
                raise Exception('name is required')
        
    def collect_task(self, tasks: List[Task]) -> None:
          self.tasks.extend(tasks)
          
    def count_pending_tasks(self) -> int:
        count = 0
        for task in self.tasks:
            print(task.description)
            if not task.iscompleted():  
                count += 1
        return count  

# usuario_1 = User(id=uuid4(), name='Victoria')
# usuario_2 = User(id=uuid4(), name='Alexandre')


# usuario_1.name #Printar o nome do usuario1 
# usuario_2.name #Printar o nome do usuario2 

# usuario_3 = User(id=4, name='usuario invalido')

# usuario_3.validate() # erro id must be an UUID

# usuario_2 = User(id=5, name='Roney') # erro id must be an UUID
