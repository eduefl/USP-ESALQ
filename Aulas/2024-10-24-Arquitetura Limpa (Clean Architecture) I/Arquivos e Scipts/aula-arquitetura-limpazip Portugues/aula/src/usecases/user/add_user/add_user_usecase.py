from domain.user.user_repository_iterface import UserRepositoryInterface
from domain.__seedwork.user_case_interface import UseCaseInterface
# from typing import Any
from usecases.user.add_user.add_user_dto import AddUserInputDto, AddUserOutputDto
from domain.user.user_entity import User
import uuid

class AddUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface
    def __init__ (self, user_repository: UserRepositoryInterface):
        self.user_repository= user_repository

    def execute(self,input: AddUserInputDto) -> AddUserOutputDto:

        user = User(id = uuid.uuid4(), nome= input.name)

        self.user_repository.add_user(user =user)
        # Melhor tratar os erros na validacao da entidade e no repositorio evitar tratar erro no caso de uso -(mas se quiser pode) 

        return AddUserOutputDto(id= user.id, name = user.name)



# user_repository = UserRepository(session=session)
# usecase = AddUserUseCase(user_repository = user_repository)
# output: AddUserUserOutputDto = usecase.execute(input = AddUserUserOutputDto(name='rafaela'))
# output.id
# output.name
