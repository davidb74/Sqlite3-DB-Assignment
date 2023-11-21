import sqlite3

CREATE_FAST_FOODS_TABLE = "CREATE TABLE IF NOT EXISTS fast_foods (id INTEGER PRIMARY KEY, name TEXT, price REAL, calories INTEGER, sizes_available TEXT);"

INSERT_FAST_FOOD = "INSERT INTO fast_foods (name, price, calories, sizes_available) VALUES (?, ?, ?, ?);"
UPDATE_FAST_FOOD = "UPDATE fast_foods SET name = ?, price = ? WHERE id = ?"

GET_ALL_FAST_FOODS = "SELECT * FROM fast_foods;"
GET_FAST_FOODS_BY_NAME = "SELECT * FROM fast_foods WHERE name = ?;"
DELETE_FAST_FOODS_BY_NAME = "DELETE FROM fast_foods WHERE name = ?"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_FAST_FOODS_TABLE)

def add_fast_food(connection, name, price, calories, sizes_available):
    with connection:
        connection.execute(INSERT_FAST_FOOD, (name, price, calories, sizes_available))

def update_fast_food(connection, new_name, new_price, old_name):
    with connection:
        connection.execute(UPDATE_FAST_FOOD, (new_name, new_price, old_name))

def get_all_fast_foods(connection):
    with connection:
        return connection.execute(GET_ALL_FAST_FOODS).fetchall()

def get_fast_foods_by_name(connection, name):
    with connection:
        return connection.execute(GET_FAST_FOODS_BY_NAME, (name,)).fetchall()

def delete_fast_foods_by_name(connection, name):
    with connection:
        connection.execute(DELETE_FAST_FOODS_BY_NAME, (name,)).fetchone()
        return connection.execute(GET_FAST_FOODS_BY_NAME, (name,)).fetchall()








