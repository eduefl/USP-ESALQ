import pytest
import uuid

from domain.task.task_entity import Task

class TestTask:
    # Teste para verificar o construtor da classe tarefa
    def test_task_initialization(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = 'tem que ter disposicao'
        completed = False        

        task = Task(
            id          =   task_id,
            user_id     =  user_id,
            title       = title,
            description     = description,
            completed    =completed,
        )

        assert task.id          == task_id
        assert task.user_id     == user_id    
        assert task.title       == title      
        assert task.description == description
        assert task.completed   == completed  
        
    # Teste Para validacao ID da tarefa 
    def test_task_id_validation(self):
        task_id = 'Errado'
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = 'tem que ter disposicao'
        completed = False        
        with pytest.raises(Exception, match= 'id must be an UUID.'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )
            
            

    def test_task_userid_validation(self):
        task_id = uuid.uuid4()
        user_id = 'eRRADO'         
        title = 'invadi o morrao'
        description = 'tem que ter disposicao'
        completed = False        
        with pytest.raises(Exception, match= 'Userid must be an UUID.'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )
            

    def test_task_title_validation(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = uuid.uuid4()
        description = 'tem que ter disposicao'
        completed = False        
        with pytest.raises(Exception, match= 'Title must be an String'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )

    def test_task_title_validation2(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = ''
        description = 'tem que ter disposicao'
        completed = False        
        with pytest.raises(Exception, match= 'Title must not be empty'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )


    def test_task_title_validation3(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'abc'
        description = 'tem que ter disposicao'
        completed = False        
        with pytest.raises(Exception, match= 'Title must have at least 5 positions'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )


    def test_task_Description_validation(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = uuid.uuid4()         
        completed = False        
        with pytest.raises(Exception, match= 'Description must be an String'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )

    def test_task_Description_validation2(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = ''         
        completed = False        
        with pytest.raises(Exception, match= 'Description must not be empty'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )

    def test_task_Description_validation3(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = 'invadi o '         
        completed = False        
        with pytest.raises(Exception, match= 'Description must have at least 5 positions'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )


    def test_task_completed_validation(self):
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = 'tem que ter disposicao'
        completed = 'False'        
        with pytest.raises(Exception, match= 'Completed must eb a boolean argument'):
            task = Task(
                id          =   task_id,
                user_id     =  user_id,
                title       = title,
                description     = description,
                completed    =completed,
            )
    # Teste para verificar se uma tarefa foi completada com a funcao mark_as_completed
        task_id = uuid.uuid4()
        user_id = uuid.uuid4()         
        title = 'invadi o morrao'
        description = 'tem que ter disposicao'
        completed = False            
        task = Task(
            id          =   task_id,
            user_id     =  user_id,
            title       = title,
            description     = description,
            completed    =completed,
        )
        
        task.mark_as_completed()
        assert task.completed          == True        


