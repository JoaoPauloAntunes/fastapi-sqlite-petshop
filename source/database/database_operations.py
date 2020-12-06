import sqlite3

from dependencies import database_path, id_checker


async def get_last_inserted():
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        last_id = cursor.lastrowid
    except Exception as error:
        print("ErrorLastID", error)
        last_id = ""
    finally:
        cursor.close()
        connection.close()
    return last_id


async def create_new_customer(data):
    parsed_data = [str(data.name), int(data.age), str(data.avatar)]

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    try:
        sql = "insert into customer(name, age, avatar) values(?,?,?)"
        cursor.execute(sql, parsed_data)
        connection.commit()
        state = True
        new_id = cursor.lastrowid
        id_checker.set_id(int(new_id))
    except Exception as error:
        print("ErrorCreate", error)
        state = False
    finally:
        cursor.close()
        connection.close()

    if state:
        print(new_id)
        return new_id, data


async def retrieve_all_customers():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    try:
        sql = "select * from customer order by name desc"
        cursor.execute(sql)
        customer_list = cursor.fetchall()

    except Exception as error:
        print("ErrorListing" + str(error))
    finally:
        cursor.close()
        connection.close()
    
    return customer_list


async def retrieve_single_customer(user_id):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    try:
        sql = "select * from customer where user_id = ?"
        cursor.execute(sql, [user_id])
        customer = cursor.fetchone()
        if customer is None:
            state = False
        else:
            state = True
    except Exception as error:
        state = False
        print("ErrorRetrievingCustomer" + str(error))
    finally:
        cursor.close()
        connection.close()
    return state, customer


async def update_customer(data, user_id):
    print(type(data))
    parsed_data = [str(data.name), int(data.age), str(data.avatar)]
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    try:
        sql = "UPDATE customer SET name = ?, age = ?, avatar = ? WHERE user_id = {idf}".format(
            idf=str(user_id)
        )

        cursor.execute(sql, parsed_data)
        connection.commit()
        state = True
    except Exception as error:
        print("ErrorUpdating" + str(error))
        state = False
    finally:
        cursor.close()
        connection.close()
    return state


async def delete_customer(user_id):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    try:
        sql = "DELETE FROM customer WHERE user_id = ?"
        cursor.execute(sql, str(user_id))
        connection.commit()
        if cursor.rowcount > 0:
            deleted = True
        else:
            deleted = False
    except Exception as error:
        print("ErrorDelete", error)
        deleted = False
    finally:
        cursor.close()
        connection.close()

    return deleted
