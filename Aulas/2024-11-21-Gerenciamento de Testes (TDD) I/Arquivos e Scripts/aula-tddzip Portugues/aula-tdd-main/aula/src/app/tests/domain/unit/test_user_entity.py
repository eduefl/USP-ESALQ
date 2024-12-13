import pytest
import uuid

from domain.user.user_entity import User

class Testuser:
    # Teste para constriir o Usuario
    def test_user_initialization(self):
        user_id = uuid.uuid4()
        user_name = "Xandao"
        user = User(id = user_id, name = user_name)

        assert  user.id == user_id
        assert  user.name == user_name        


    # Teste para validacao do ID do usuario 
    def test_user_id_validation(self):
        user_id = 'Id_invalido'
        user_name = "Invalido"
        with pytest.raises(Exception, match ='id must be an UUID.'):
            User(id = user_id, name = user_name)

    # Teste para validacao do nome do usuario
    def test_user_name_validation(self):
        user_id = uuid.uuid4()
        user_name = ""
        with pytest.raises(Exception, match ='name is required'):
            User(id = user_id, name = user_name)
 

    def test_user_name_validation2(self):
        user_id = uuid.uuid4()
        user_name = 3
        with pytest.raises(Exception, match ='name Need to be an String'):
            User(id = user_id, name = user_name)
