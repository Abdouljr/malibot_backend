from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from configurations.database_config import db_dependency
from models.user import UserBase
from services import auth_service

router = APIRouter(prefix='/auth', tags=['Authentification'])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def sign_in(userBase: UserBase, db: Session = db_dependency):
    return auth_service.sign_in(userBase, db)


@router.post("/token")
async def connexion(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = db_dependency):
    return auth_service.login(form_data.username, form_data.password, db)
