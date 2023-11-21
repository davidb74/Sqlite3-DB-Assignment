import database

MENU_PROMPT = """-----------------------------------------------
-- Fast Food App --

Please choose one of these options:

1) Add a new fast food product.
2) Update a fast food product.
3) See all fast food products.
4) Find a fast food product by name.
5) Delete a fast food product by name.
6) Exit. 

Your selection: """

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            prompt_add_new_fast_food(connection)
        elif user_input == "2":
            prompt_update_fast_food(connection)
        elif user_input == "3":
            prompt_see_all_fast_foods(connection)
        elif user_input == "4":
            prompt_find_fast_food(connection)
        elif user_input == "5":
            prompt_delete_fast_food(connection)
        else:
            print("Invalid input, please try again!")


def prompt_add_new_fast_food(connection):
    name = input("Enter the fast food product's name: ")
    price = input("Enter the price: ")
    calories = int(input("Enter the calories of the fast food product: "))
    sizes_available = input("Enter the size available (SM, M, L, XL or N/A): ")

    database.add_fast_food(connection, name, price, calories, sizes_available)

def prompt_update_fast_food(connection):
    name = input("Enter the fast food product's name to update: ")

    existing_fast_foods = database.get_fast_foods_by_name(connection, name)
    if not existing_fast_foods:
        print(f"No fast food product with the name '{name}' found.")
        return

    new_name = input("Enter the new name (press Enter to keep the current name): ")
    new_price = input("Enter the new price (press Enter to keep the current price): ")
    print(new_price)
    existing_fast_food = existing_fast_foods[0]
    existing_name, existing_price = existing_fast_food[1], existing_fast_food[2]

    updated_name = new_name if new_name else existing_name
    updated_price = new_price if new_price else existing_price

    database.update_fast_food(connection, updated_name, updated_price, name)
    print(f"Fast food product '{name}' updated successfully.")

    prompt_see_all_fast_foods(connection)

def prompt_see_all_fast_foods(connection):
    fast_foods = database.get_all_fast_foods(connection)

    for fast_food in fast_foods:
        updated_name = fast_food[1]
        updated_price = fast_food[2]
        print(f"{updated_name} ({updated_price}) - {fast_food[3]} cals - Size: {fast_food[4]}")
        #print(f"{fast_food[1]} ({fast_food[2]}) - {fast_food[3]} cals - Size: {fast_food[4]}")

def prompt_find_fast_food(connection):
    name = input("Enter fast food product's name to find: ")
    fast_foods = database.get_fast_foods_by_name(connection, name)

    for fast_food in fast_foods:
        print(f"{fast_food[1]} ({fast_food[2]}) - {fast_food[3]} cals - Size: {fast_food[4]}")

def prompt_delete_fast_food(connection):
    name = input("Enter fast food product's name to delete: ")
    fast_foods = database.delete_fast_foods_by_name(connection, name)

    for fast_food in fast_foods:
        print(f"{fast_food[1]} ({fast_food[2]}) - {fast_food[3]} cals - Size: {fast_food[4]}")

menu()