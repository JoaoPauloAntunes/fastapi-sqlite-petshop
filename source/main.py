from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import uvicorn

from source.database_routes import db_router
from source.file_routes import file_router
from source.views_render import views_router
from source.dependencies import id_checker

app = FastAPI()

app.mount("/static", StaticFiles(directory="source/static"), name="static")

app.include_router(db_router, prefix="/customer", tags=["Customer CRUD"])
app.include_router(file_router, prefix="/file", tags=["File management"])
app.include_router(views_router, prefix="/views", tags=["Views"])


viewstemplate = Jinja2Templates(directory="source/views")

app.mount("/data", StaticFiles(directory="source/data"), name="data")


@app.get("/")
async def index():
    return {threading.active_count()}


@app.get("/last_id")
async def last_id():
    return id_checker.get_id()


@app.get("/home")
async def home(request: Request):
    return viewstemplate.TemplateResponse("home.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)
