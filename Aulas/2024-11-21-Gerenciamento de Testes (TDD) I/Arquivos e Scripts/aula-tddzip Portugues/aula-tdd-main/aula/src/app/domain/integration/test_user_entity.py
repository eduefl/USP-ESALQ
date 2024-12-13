# from aula.src.app.domain.user.user_entity import User
from domain.user.user_entity import User
from domain.task.task_entity import Task
import uuid

class TestUserWithTasks:
    # Teste para adicionar tarefas ao usuario
    def test_collect_tasks(self):
        user_id = uuid.uuid4()
        user_name = "Integrador"
        user = User(id = user_id, name = user_name)
        
        task_id = uuid.uuid4()
        user_id = user_id
        title = 'Integrar'
        description = 'Tem que integrar para interar'
        completed = False        
        task1 = Task(
            id          =   task_id,
            user_id     =  user_id,
            title       = title,
            description     = description,
            completed    =completed,
        )        

        task_id = uuid.uuid4()
        user_id = user_id
        title = 'Reintegrare'
        description = 'A constancia e necessaria'
        completed = False        
        task2 = Task(
            id          =   task_id,
            user_id     =  user_id,
            title       = title,
            description     = description,
            completed    =completed,
        )
        
        user.collect_tasks([task1,task2])
        
        assert len(user.tasks) == 2 
        
        assert task1 in user.tasks
        assert task2 in user.tasks
        
