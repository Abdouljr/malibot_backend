from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from configurations.database_config import db_dependency
from models.groupe import GroupeDTO, GroupeBase
from models.user import UserDTO
from services import groupe_service, auth_service


router = APIRouter(prefix='/groupe', tags=['Groupe'])
user_dependency = Annotated[dict, Depends(auth_service.get_current_user)]
message_erreur = "non authentifié"


@router.post("/add", response_model=GroupeDTO, status_code=status.HTTP_201_CREATED)
async def add(groupe: GroupeBase, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    print(user)
    return groupe_service.add(user['uid'], groupe, db)


@router.get("/all", response_model=List[GroupeDTO], status_code=status.HTTP_200_OK)
async def get_all(user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return groupe_service.get_all(db)


@router.get("/get-for-user", response_model=List[GroupeDTO], status_code=status.HTTP_200_OK)
async def get_for_user(user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return groupe_service.get_groupes_for_user(db, user['uid'])


@router.get("/add-user-to-groupe", response_model=List[UserDTO], status_code=status.HTTP_200_OK)
async def add_user_to_groupe(groupe_id: int, user_email: str, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return groupe_service.add_users_to_groupe(db, groupe_id, user_email)


@router.delete("/delete/{groupe_id}", status_code=status.HTTP_200_OK)
async def delete(user: user_dependency, groupe_id: int, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return groupe_service.supprimer_groupe(groupe_id, db)
