from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from configurations.database_config import db_dependency
from models.tache import TacheDTO, TacheBase
from services import tache_service, auth_service


router = APIRouter(prefix='/tache', tags=['Tache'])
user_dependency = Annotated[dict, Depends(auth_service.get_current_user)]
message_erreur = "non authentifié"


@router.post("/add", response_model=TacheDTO, status_code=status.HTTP_201_CREATED)
async def add(tache: TacheBase, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return tache_service.add(tache, db)


@router.put("/update", response_model=TacheDTO, status_code=status.HTTP_200_OK)
async def update(tache: TacheDTO, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return tache_service.update(tache, db)


@router.get("/get-by-groupe/{groupe_id}", response_model=List[TacheDTO], status_code=status.HTTP_200_OK)
async def get_by_groupe(groupe_id: int, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return tache_service.get_by_groupe(groupe_id, db)


@router.delete("/delete/{tache_id}", status_code=status.HTTP_200_OK)
async def delete(user: user_dependency, tache_id: int, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message_erreur)
    return tache_service.delete(tache_id, db)
