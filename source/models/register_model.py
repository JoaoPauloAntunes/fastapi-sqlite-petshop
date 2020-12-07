from source.models.database_operations import (
    create_new_customer,
    update_avatar,
    retrieve_all_pets,
)
from source.models.schemas import PetSchema
from source.models.file_handling import avatar_creation


async def create_new_pet(files, name, age):

    new_pet = PetSchema(name=name, age=age, avatar="sample")
    user_id, insert_status = await create_new_customer(new_pet)
    if insert_status:
        avatar_path, avatar_status = avatar_creation(files, user_id)
        if avatar_status:
            update_status = await update_avatar(avatar_path, user_id)
    return user_id, insert_status


async def get_all_pets():
    response = await retrieve_all_pets()
    return response
