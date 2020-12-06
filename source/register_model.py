from file_handling import file_uploader
from database.database_operations import create_new_customer


async def register_process(customer, file):

    user_id, _ = await create_new_customer(customer)
    response = file_uploader(file, int(user_id))
    return response
