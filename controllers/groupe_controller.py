from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from configurations.database_config import db_dependency
from models.groupe import GroupeDTO, GroupeBase
from services import groupe_service, auth_service


router = APIRouter(prefix='/groupe', tags=['Groupe'])
user_dependency = Annotated[dict, Depends(auth_service.get_current_user)]


@router.post("/add", response_model=GroupeDTO, status_code=status.HTTP_201_CREATED)
async def add(groupe: GroupeBase, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    print(user)
    return groupe_service.add(user['uid'], groupe, db)


@router.get("/all", response_model=List[GroupeDTO], status_code=status.HTTP_200_OK)
async def get_all(user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    return groupe_service.get_all(db)


@router.delete("/delete/{groupe_id}", status_code=status.HTTP_200_OK)
async def delete(user: user_dependency, groupe_id: int, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    return groupe_service.supprimer_groupe(groupe_id, db)
