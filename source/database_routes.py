from fastapi import FastAPI, APIRouter, Body
from database.schemas import CustomerSchema, putCustomerSchema
from database.database_operations import (
    create_new_customer,
    retrieve_all_customers,
    retrieve_single_customer,
    update_customer,
    delete_customer,
    get_last_inserted,
)

db_router = APIRouter()


@db_router.post("/insert", response_description="right here")
async def post_customer(customer: CustomerSchema = Body(...)):
    response = await create_new_customer(customer)
    return response


@db_router.get("/list")
async def get_all_customers():
    response = await retrieve_all_customers()
    return response


@db_router.get("/search")
async def search_entry(id: int):
    response = await retrieve_single_customer(id)
    return response


@db_router.put("/update")
async def put_customer(customer: putCustomerSchema, user_id: int):
    response = await update_customer(customer, user_id)
    return response


@db_router.delete("/delete")
async def del_customer(id: int):
    response = await delete_customer(id)
    return response
