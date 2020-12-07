from fastapi import FastAPI, APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import List

from source.models.register_model import create_new_pet, get_all_pets
from source.models.schemas import OutputModel, ResponseModel

register_router = APIRouter()


@register_router.post("/create_pet/", response_model=OutputModel, status_code=201)
async def receive_creation_data(
    files: List[UploadFile] = File(...),
    name: str = Form(...),
    age: int = Form(...),
):
    new_pet, status = await create_new_pet(files, name, age)
    if status:
        code = 201
    else:
        code = 400
    return {"data": new_pet, "status": code}


@register_router.get("/pets_list")
async def list_all_pets():
    data, state = await get_all_pets()
    if state:
        code = 200
        if not data:
            code = 204
    else:
        code = 400
    # return {"data": response, "status": code}
    return ResponseModel(data, code)
