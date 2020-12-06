from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import threading
import uvicorn

from database_routes import db_router
from file_routes import file_router
from views_render import views_router
from dependencies import id_checker

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(db_router, prefix="/customer", tags=["Customer CRUD"])
app.include_router(file_router, prefix="/file", tags=["File management"])
app.include_router(views_router, prefix="/views", tags=["Views"])


templates = Jinja2Templates(directory="views")
app.mount("/data", StaticFiles(directory="data"), name="data")


@app.get("/")
async def index():
    return {threading.active_count()}


@app.get("/last_id")
async def last_id():
    return id_checker.get_id()


@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)
