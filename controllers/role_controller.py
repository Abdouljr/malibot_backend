from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from configurations.database_config import db_dependency
from models.role import RoleDTO, RoleBase
from services import role_service, auth_service


router = APIRouter(prefix='/role', tags=['Role'])
user_dependency = Annotated[dict, Depends(auth_service.get_current_user)]


@router.post("/add", response_model=RoleDTO, status_code=status.HTTP_201_CREATED)
async def ajouter_role(role: RoleBase, user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    return role_service.add(role, db)


@router.get("/all", response_model=List[RoleDTO], status_code=status.HTTP_200_OK)
async def lister_roles(user: user_dependency, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    return role_service.get_all(db)


@router.delete("/delete/{role_id}", status_code=status.HTTP_200_OK)
async def supprimer_role(user: user_dependency, role_id: int, db: Session = db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non authentifié")
    return role_service.supprimer_role(role_id, db)
