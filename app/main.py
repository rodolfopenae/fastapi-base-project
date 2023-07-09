from fastapi import FastAPI
from api.v1.users import router as users_v1
from api.v1.workspace import router as workspaces_v1
from api.v1.auth import router as auth_v1
from kernel.infraestructure.postgres_database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(
    title="Observers"
)

app.include_router(auth_v1, tags=['Auth'])
app.include_router(users_v1, tags=['User'])
app.include_router(workspaces_v1, tags=['Workspaces'])
