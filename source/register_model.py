from source.models.database_operations import create_new_customer, update_avatar
from source.models.schemas import PetSchema
from source.file_handling import avatar_creation


async def create_new_pet(files, name, age):

    new_pet = PetSchema(name=name, age=age, avatar="sample")
    user_id, insert_status = await create_new_customer(new_pet)
    if insert_status:
        avatar_path, avatar_status = avatar_creation(files, user_id)
        if avatar_status:
            update_status = await update_avatar(avatar_path, user_id)
    return user_id, insert_status
