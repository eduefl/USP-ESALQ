import typing
import uuid
from domain.task.task_entity import Task

class User:
    id: uuid.UUID
    name: str 
    tasks: typing.List[Task]

    def __init__(self, id: uuid.UUID,  name: str):
        self.id = id
        self.name = name        
        self.tasks = []
        self.validate()
    
    def validate(self):
        if not isinstance(self.id, uuid.UUID):
            raise Exception('id must be an UUID.')
        if not isinstance(self.name, str):
            raise Exception('name Need to be an String')
        if len(self.name) == 0:
            raise Exception('name is required')
        
    def collect_tasks(self, tasks: typing.List[Task]) -> None:
        print(self.tasks)
        self.tasks.extend(tasks)
        pass

# user = User(id = uuid.uuid4(), name= 'Macha')

# print(user.id)
# print(user.name)