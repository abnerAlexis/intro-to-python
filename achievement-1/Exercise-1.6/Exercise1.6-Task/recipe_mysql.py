import mysql.connector

def create_database_and_table(conn, cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    cursor.execute("USE task_database")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)
    conn.commit()


def main_menu():
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='beren',
        database='task_database'
    )
    cursor = conn.cursor()


    menu_options = {
        '1': create_recipe,
        '2': search_recipe,
        '3': update_recipe,
        '4': delete_recipe
    }

    while True:
        print_menu()
        selection = get_user_selection()

        if selection in menu_options:
            try:
                menu_options[selection](conn, cursor)
            except Exception as e:
                print(f"Error: {e}")
        elif selection == '5':
            print("Exiting...")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            # print("Invalid entry, please try again.")
            cursor.execute("DESCRIBE Recipes")


def print_menu():
    print("\nOptions:")
    print("1. Create a new recipe")
    print("2. Search for recipes by ingredient")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("5. Exit")


def get_user_selection():
    return input("Enter a number (1-5): ")


def calc_difficulty(cook_time, ingredients):
    ingredient_count = len(ingredients.split(', '))

    if cook_time < 10 and ingredient_count < 4:
        return "Easy"
    elif cook_time < 10 and ingredient_count >= 4:
        return "Medium"
    elif cook_time >= 10 and ingredient_count < 4:
        return "Intermediate"
    elif cook_time >= 10 and ingredient_count >= 4:
        return "Hard"
    else:
        return "Difficulty Unknown"
    

def format_ingredients(ingredients):
    # strip any leading or trailing whitespace from each ingredient and excluding any empty strings
    return ', '.join(ingredient.strip() for ingredient in ingredients.split(',') if ingredient.strip())


def create_recipe(conn, cursor):
    # Prompt user
    name = input("Enter the recipe name: ")
    while not name:
        print("Recipe name cannot be empty.")
        name = input("Enter the recipe name: ")

    cooking_time = 0
    # Retrive a valid cooking time from the user
    while cooking_time <= 0:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            if cooking_time <= 0:
                print("Cooking time must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    ingredients = input("Enter the ingredients (e.g. ingredient1, ingredient2)): ")
    formatted_ingredients = format_ingredients(ingredients) 

    try:
        difficulty = calc_difficulty(cooking_time, formatted_ingredients)

        insert_query = """
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, formatted_ingredients, cooking_time, difficulty))
        conn.commit()
        print("Recipe added successfully!")
        print("Recipe Details:")
        print("Name:", name)
        print("Ingredients:", formatted_ingredients)
        print("Cooking Time:", cooking_time, "minutes")
        print("Difficulty:", difficulty)
    except Exception as e:
        print("An error occurred:", e)


def search_recipe(conn, cursor):
    # Retrieve all distinct ingredients
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Create a set of ingredients
    all_ingredients = set()
    for row in results:
        ingredients = row[0]
        # Convert each ingredient to lowercase before adding it to the set
        all_ingredients.update(ingredient.strip().lower() for ingredient in ingredients.split(', '))

    if not all_ingredients:
        print("\nNo ingredients available. Please add a recipe first.")
        return

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f"{i}. {ingredient}")

    selection = int(input("Enter the number of an ingredient to search: ")) - 1
    search_ingredient = sorted(all_ingredients)[selection]

    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(search_query, ('%' + search_ingredient + '%',))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No recipes found with that ingredient.")


def update_recipe(conn, cursor):

    recipes = fetch_recipes(cursor)
    
    if not recipes:
        print("No recipes available to update.")
        return
    
    print_recipes(recipes)

    # Prompt the user to enter the ID of the recipe they want to update
    recipe_id = int(input("Enter the ID of the recipe to update: "))
    
    # Ask the user which column they want to update
    column_to_update = input("Enter the column to update (name, ingredients, cooking_time): ")

    if column_to_update == 'name':
        update_name(cursor, recipe_id)
    elif column_to_update == 'ingredients':
        update_ingredients(cursor, recipe_id)
    elif column_to_update == 'cooking_time':
        update_cooking_time(cursor, recipe_id)
    else:
        # If the user enters an invalid column, print an error message and exit the function
        print("Invalid column.")
        return

    # If the user updated the ingredients or cooking time, recalculate the recipe's difficulty
    if column_to_update in ['ingredients', 'cooking_time']:
        update_difficulty(cursor, recipe_id)

    # Commit the transaction to save all changes permanently to the database
    conn.commit()
    
    # Notify the user that the recipe was updated successfully
    print("Recipe updated successfully!")


def fetch_recipes(cursor):
    # Fetch the ID and name of all recipes from the Recipes table
    cursor.execute("SELECT id, name FROM Recipes")
    return cursor.fetchall()


def print_recipes(recipes):
    print("\nExisting recipes:")
    for row in recipes:
        print(f"ID: {row[0]}, Name: {row[1]}")


def update_name(cursor, recipe_id):
    # If the column to update is 'name', prompt the user for the new name
    new_value = input("Enter the new name: ")
    # Update the name in the Recipes table where the ID matches the recipe_id
    update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, recipe_id))


def update_ingredients(cursor, recipe_id):
     # If the column to update is 'ingredients', prompt the user for the new ingredients
    new_value = input("Enter the new ingredients (comma-separated): ")
    
    # format the new ingredients input 
    formatted_ingredients = format_ingredients(new_value)
    
    # Update the ingredients in the Recipes table where the ID matches the recipe_id
    update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
    cursor.execute(update_query, (formatted_ingredients, recipe_id))


def update_cooking_time(cursor, recipe_id):
    # If the column to update is 'cooking_time', prompt the user for the new cooking time
    new_value = int(input("Enter the new cooking time (in minutes): "))
    # Update the cooking_time in the Recipes table where the ID matches the recipe_id
    update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
    cursor.execute(update_query, (new_value, recipe_id))


def update_difficulty(cursor, recipe_id):
    # Fetch the updated cooking time and ingredients for the recipe
    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
    row = cursor.fetchone()
    
    # Calculate the difficulty based on the cooking time and ingredients
    difficulty = calc_difficulty(row[0], row[1])
    
    # Update the difficulty in the Recipes table where the ID matches the recipe_id
    update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
    cursor.execute(update_query, (difficulty, recipe_id))


def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    
    if not recipes:
        print("\nNo recipes available to delete.")
        return
    
    print("\nExisting recipes:")
    for row in recipes:
        print(f"ID: {row[0]}, Name: {row[1]}")

    recipe_id = int(input("Enter the ID of the recipe to delete: "))

    delete_query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(delete_query, (recipe_id,))
    conn.commit()
    print("Recipe deleted")    


def main():
    main_menu()


if __name__ == "__main__":
    main()