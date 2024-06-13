from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.team import router as team_router

app = FastAPI()

app.include_router(user_router)
app.include_router(team_router)