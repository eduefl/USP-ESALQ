import uuid

class Task:
    id          : uuid.UUID
    user_id     : uuid.UUID
    title       : str
    description : str
    completed   : bool

    def __init__(self,          
                 id: uuid.UUID,
                 user_id     : uuid.UUID,
                 title       : str,
                 description : str,
                 completed   : bool):
        self.id             = id
        self.user_id        = user_id    
        self.title          = title      
        self.description    = description
        self.completed      = completed  
        self.validate()
        pass
    
    def validate(self):
        if not isinstance(self.id, uuid.UUID):
            raise Exception ('id must be an UUID.')
        if not isinstance(self.user_id, uuid.UUID):
            raise Exception ('Userid must be an UUID.')        
        if not isinstance(self.title, str):
            raise Exception ('Title must be an String')                
        if len(self.title) == 0:
            raise Exception ('Title must not be empty')                        
        if len(self.title) < 5:
            raise Exception ('Title must have at least 5 positions')                                
        if not isinstance(self.description, str):
            raise Exception ('Description must be an String')                
        if len(self.description) == 0:
            raise Exception ('Description must not be empty')                        
        if len(self.description) < 10:
            raise Exception ('Description must have at least 5 positions')                                        
        if not isinstance(self.completed, bool):
            raise Exception ('Completed must eb a boolean argument')
        
    def mark_as_completed(self):
        self.completed = True
        pass        