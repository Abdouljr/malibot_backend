from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from configurations.database_config import engine, SessionLocal
from controllers import role_controller, auth_controller, groupe_controller
from models import user, role, groupe, tache, favori
from services import role_service


@asynccontextmanager
async def lifespan(main: FastAPI):
    role_service.init()
    print("Application started!")
    yield
    print("Application stopped!")


app = FastAPI(lifespan=lifespan, title="MaliBot", version="1.0.0")

app.include_router(auth_controller.router)
app.include_router(role_controller.router)
app.include_router(groupe_controller.router)

user.Base.metadata.create_all(bind=engine)
role.Base.metadata.create_all(bind=engine)
groupe.Base.metadata.create_all(bind=engine)
tache.Base.metadata.create_all(bind=engine)
favori.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)
