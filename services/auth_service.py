import uuid
from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from starlette import status

from configurations.database_config import SessionLocal
from models.user import UserBase, User
from models.role import Role
from jose import jwt, JWTError
import bcrypt
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix='/auth', tags=['Authentification'])
SECRET_KEY = '77217A24432646294A404E635266556A586E3272357538782F413F442A472D4B'
ALGORITHM = 'HS256'
REFRESH_TOKEN_EXPIRE_DAYS = 7
ACCESS_TOKEN_EXPIRE_MINUTES = 30
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
Oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


# sign in
def sign_in(user: UserBase, db):
    exist_user = (db.query(User).filter(User.email == user.email).first())
    db_role = db.query(Role).filter(Role.name == 'USER').first()
    if db_role is None:
        raise HTTPException(status_code=505, detail="role user non trouvé")
    if exist_user:
        raise HTTPException(status_code=505, detail='Cet adresse email est déjà utilisé')

    db_user = User(**user.model_dump())
    db_user.password = hash_password(user.password)
    db_user.unique_id = uuid.uuid1()
    db_user.role = db_role

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return get_token(db_user)


# login
def login(email: str, password: str, db):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        return False
    password_hash = db_user.password
    if not bcrypt_context.verify(password, password_hash):
        return False

    return get_token(db_user)


# generate token
def generer_token(user: User, expiration_token: timedelta):
    encode = {'sub': user.email, 'uid': user.unique_id}
    expiration = datetime.utcnow() + expiration_token
    encode.update({'exp': expiration})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# get token
def get_token(user: User):
    access = generer_token(user, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    refresh = generer_token(user, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    return {"access_token": access, "refresh_token": refresh}


# hash password
def hash_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  # Mysql
    return hashed_password


# get current user
async def get_current_user(token: Annotated[str, Depends(Oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        unique_id: str = payload.get('uid')
        if username is None or unique_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Vous n'êtes pas autorisé")

        return {'username': username, 'uid': unique_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Vous n'êtes pas autorisé")


# create default admin
def create_default_admin():
    session = SessionLocal()
    user = User(unique_id=str(uuid.uuid4()), username="Abdouljr", email="maiga@test.com",
                password=hash_password('1234'), role_id=1)
    super_admin = session.query(User).filter_by(email=user.email).first()
    if not super_admin:
        session.add(user)
        session.commit()
