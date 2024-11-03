from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from configurations.database_config import engine
from controllers import role_controller, auth_controller
from models import user, role


@asynccontextmanager
async def lifespan(main: FastAPI):
    print("Application started!")
    yield
    print("Application stopped!")


app = FastAPI(lifespan=lifespan, title="MaliBot", version="1.0.0")
app.include_router(auth_controller.router)
app.include_router(role_controller.router)
user.DataBase.metadata.create_all(bind=engine)
role.DataBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)