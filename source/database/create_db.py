import sqlite3


def create_customer_table():
    try:
        connection = sqlite3.connect("shop.db")  # creates or connect to it
        cursor = connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS customer(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT , 
            age INTEGER, 
            avatar TEXT)"""
        cursor.execute(sql)
        print("Table created!")

    except Exception as erro:
        print("Table creation fail: " + str(erro))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_customer_table()