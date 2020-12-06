from fastapi import FastAPI, APIRouter, Body, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List

from database.schemas import CustomerSchema
from register_model import register_process
from database.database_operations import create_new_customer, retrieve_all_customers

views_router = APIRouter()
templates = Jinja2Templates(directory="views")
views_router.mount("/static", StaticFiles(directory="static"), name="static")


@views_router.get("/register/", response_class=HTMLResponse)
async def main_register(request: Request):
    # return FileResponse("views/register.html")
    return templates.TemplateResponse("register.html", {"request": request})


@views_router.get("/collection/", response_class=HTMLResponse)
async def main_collection(request: Request):
    # return FileResponse("views/register.html")
    pets_from_db = await retrieve_all_customers()

    names = []
    ages = []
    avatar = []
    for row in pets_from_db:
        names.append(row[1])
        ages.append(row[2])
        avatar.append(row[3])

    pets_list = tuple(zip(names, ages, avatar))

    return templates.TemplateResponse(
        "collection.html", {"request": request, "pets": pets_list}
    )
