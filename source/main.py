from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import uvicorn

from source.routes.register_routes import register_router
from source.routes.view_routes import views_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="source/static"), name="static")
app.mount("/data", StaticFiles(directory="source/data_avatar"), name="data")
app.include_router(register_router, prefix="/pet", tags=["Pet Management"])
app.include_router(views_router, prefix="/views", tags=["Views"])


@app.get("/")
async def index():
    return {}


@app.get("/thread")
async def thread():
    return {threading.active_count()}
