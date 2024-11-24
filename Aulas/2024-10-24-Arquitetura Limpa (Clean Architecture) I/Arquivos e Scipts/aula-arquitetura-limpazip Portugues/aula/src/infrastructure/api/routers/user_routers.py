from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.api.database import get_session
from usecases.user.add_user.add_user_dto import AddUserInputDto
from usecases.user.update_user.update_user_dto import UpdateUserInputDto
from infrastructure.user.sqlalchemy.user_repository import UserRepository
from usecases.user.add_user.add_user_usecase import AddUserUseCase
from usecases.user.update_user.update_user_usecase import UpdateUserUseCase
from uuid import UUID
from usecases.user.find_user.find_user_dto import FindUserInputDto
from usecases.user.find_user.find_user_usecase import FindUserUseCase
from usecases.user.list_users.list_users_usecase import LisUsersUseCase
from usecases.user.list_users.list_users_dto import ListUsersInputDto
from infrastructure.api.presenters.user_presenter import UserPresenter
from infrastructure.task.sqlalchemy.task_repository import TaskRepository

router = APIRouter(prefix = "/users", tags=["Users"])
#http://localhost:8000/users/upd
@router.post("/upd")
def upd_user(request: UpdateUserInputDto, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session= session)
        usecase = UpdateUserUseCase(user_repository=user_repository)
        output = usecase.execute(input = request)
        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



#http://localhost:8000/users/
@router.post("/")

def add_user(request: AddUserInputDto, session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session= session)
        usecase = AddUserUseCase(user_repository=user_repository)
        output = usecase.execute(input = request)
        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

#  encontrar usuario
#http://localhost:8000/users/{user_id}
@router.get("/{user_id}")
def find_user(user_id: UUID,session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session= session)
        task_repository = TaskRepository(session= session)
        usecase = FindUserUseCase(user_repository=user_repository,task_repository=task_repository)
        output = usecase.execute(input = FindUserInputDto(id = user_id))

        # output_json = UserPresenter.toJSOn(user_dto=output)

        # output_xml = UserPresenter.toXML(user_dto=output)

        # output_json_pt_br = UserPresenter.toJSOnPTBR(user_dto=output)

        # return {"json":output_json, "xml": output_xml, "SoNoBrasil":output_json_pt_br}
        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#http://localhost:8000/users/    
# Listar usuarios
@router.get("/")
def list_user(session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(session= session)
        usecase = LisUsersUseCase(user_repository=user_repository)
        output = usecase.execute(input = ListUsersInputDto())
        return output

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
