from fastapi import FastAPI, APIRouter, Body, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from file_handling import file_uploader
from database.database_operations import (
    get_last_inserted,
    update_customer,
    retrieve_single_customer,
)
from database.schemas import putCustomerSchema
from typing import List
from dependencies import id_checker

file_router = APIRouter()


@file_router.post("/uploadfile/")
async def upload_file(files: List[UploadFile] = File(...)):
    # user_id = await get_last_inserted()
    user_id = id_checker.get_id()
    for file in files:
        avatar = str(file_uploader(file, user_id))
    customer = await retrieve_single_customer(user_id)
    customer_data = customer[1]

    name = customer_data[1]
    age = customer_data[2]

    item = putCustomerSchema(name=name, age=age, avatar=avatar)
    _ = await update_customer(item, user_id)
    customer = await retrieve_single_customer(user_id)
    print(customer)

    return FileResponse("views/redirectComponent.html")


@file_router.get("/uploadpage", response_class=HTMLResponse)
async def upload_page():
    # return HTMLResponse(content=content)
    return FileResponse("src/templates/upload_image.html")


@file_router.get("/last_pic")
async def stream():
    path = "receive.png"
    file_like = open(path, mode="rb")
    return StreamingResponse(file_like, media_type="image/png")