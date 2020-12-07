from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import uvicorn


from source.file_routes import file_router
from source.views_render import views_router
from source.dependencies import id_checker

app = FastAPI()

app.mount("/static", StaticFiles(directory="source/static"), name="static")
app.mount("/data", StaticFiles(directory="source/data_avatar"), name="data")
app.include_router(file_router, prefix="/file", tags=["File management"])
app.include_router(views_router, prefix="/views", tags=["Views"])


@app.get("/")
async def index():
    return {}


@app.get("/thread")
async def thread():
    return {threading.active_count()}
