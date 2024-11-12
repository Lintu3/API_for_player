from fastapi import FastAPI
from .routers import players
from .database import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(players.router)