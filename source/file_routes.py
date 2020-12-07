from fastapi import FastAPI, APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import List

from source.register_model import create_new_pet
from source.models.schemas import OutputModel

file_router = APIRouter()


@file_router.post("/create_pet/", response_model=OutputModel)
async def receive_creation_data(
    files: List[UploadFile] = File(...),
    name: str = Form(...),
    age: int = Form(...),
):
    new_pet = await create_new_pet(files, name, age)
    return {"new_id": new_pet[0], "status": new_pet[1]}


#    return FileResponse("source/views/redirectComponent.html")
