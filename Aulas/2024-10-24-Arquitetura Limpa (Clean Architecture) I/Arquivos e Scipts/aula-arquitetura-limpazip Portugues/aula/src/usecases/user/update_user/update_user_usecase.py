from domain.__seedwork.use_case_interface import UseCaseInterface
from domain.user.user_repository_iterface import UserRepositoryInterface
from usecases.user.update_user.update_user_dto import UpdateUserInputDto, UpdateUseroUTPUTDto
from domain.user.user_entity import User

class UpdateUserUseCase(UseCaseInterface):

    def __init__(self,user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: UpdateUserInputDto) -> UpdateUseroUTPUTDto:

        user = User(id = input.id, name= input.name) 

 
        self.user_repository.update_user(user = user)

        return UpdateUseroUTPUTDto(id = user.id, name = user.name)