import mysql.connector

conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='beren',
        database='task_database'
    )
cursor = conn.cursor()

def print_menu():
    print("\nOptions:")
    print("1. Create a new recipe")
    print("2. Search for recipes by ingredient")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("5. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-5): ")
    return choice

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
        return "Unknown"
    
def format_ingredients(ingredients):
    # stripp any leading or trailing whitespace from each ingredient and excluding any empty strings
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
        all_ingredients.update(ingredients.split(', '))

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f"{i}. {ingredient}")

    choice = int(input("Choose an ingredient by number to search: ")) - 1
    search_ingredient = sorted(all_ingredients)[choice]

    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(search_query, ('%' + search_ingredient + '%',))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No recipes found with that ingredient.")

def main():
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
        choice = get_user_choice()

        if choice in menu_options:
            try:
                menu_options[choice](conn, cursor)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '5':
            print("Exiting...")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()