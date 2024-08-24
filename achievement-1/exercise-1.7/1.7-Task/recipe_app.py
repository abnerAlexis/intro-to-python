from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql://cf-python:beren@localhost/task_database")
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))


    def __repr__(self):
        return f"<Recipe {self.id} - {self.name} (Difficulty: {self.difficulty})>"


    def __str__(self):
        return (
            f"\n{'-'*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}\n"
        )
    

    def calculate_difficulty(self):
        ingredient_count = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredient_count < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"


def create_recipe(session):
    name = prompt_recipe_name()
    cooking_time = prompt_cooking_time()
    ingredients = prompt_ingredients()

    recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")
    print("Recipe Details:")
    print(recipe_entry)


def prompt_recipe_name():
    while True:
        name = input("Enter the recipe name (max 50 characters): ")
        if len(name) > 50:
            print("Error: Name cannot exceed 50 characters.")
        elif not name:
            print("Error: Recipe name cannot be empty.")
        else:
            return name


def prompt_cooking_time():
    while True:
        cooking_time = input("Enter the cooking time (in minutes): ")
        if not cooking_time.isnumeric():
            print("Error: Cooking time must be a number.")
        elif int(cooking_time) <= 0:
            print("Error: Cooking time must be a positive integer.")
        else:
            return int(cooking_time)


def prompt_ingredients():
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or press Enter to finish): ")
        if ingredient:
            ingredients.append(ingredient)
        else:
            break
    return ", ".join(ingredients)


def view_all_recipes(session):
    recipes = session.query(Recipe).all()
    if not recipes:
        print("There are no recipes in the database.")
        return

    print("\nAll Recipes:")
    for recipe in recipes:
        print(recipe)


def search_by_ingredients(session):
    # Get all recipes from the database
    all_recipes = get_all_recipes(session)

    if not all_recipes:
        print("There are no recipes in the database.")
        return

    # Create a set of all ingredients
    all_ingredients = get_all_ingredients(all_recipes)

    # Display all ingredients
    ingredient_list = display_ingredients(all_ingredients)

    # Ask the user to select ingredients by number
    selected_numbers = get_user_selected_numbers(ingredient_list)

    # Create a list of selected ingredients
    search_ingredients = [ingredient_list[int(num) - 1] for num in selected_numbers]

    # Search for recipes that match the selected ingredients
    search_results = search_recipes_by_ingredients(session, search_ingredients)

    # Display the search results
    display_search_results(search_results)


def get_all_recipes(session):
    # Retrieve all recipes from the database.
    return session.query(Recipe).all()


def get_all_ingredients(all_recipes):
    # Create a set of all ingredients from the recipes.
    all_ingredients = set()
    for recipe in all_recipes:
        ingredients = recipe.ingredients.split(", ")
        all_ingredients.update(ingredient.lower() for ingredient in ingredients)
    return all_ingredients


def display_ingredients(all_ingredients):
    # Display the available ingredients and return a sorted list.
    print("\nAvailable Ingredients:")
    ingredient_list = sorted(all_ingredients)
    for i, ingredient in enumerate(ingredient_list, 1):
        print(f"{i}. {ingredient.capitalize()}")
    return ingredient_list


def get_user_selected_numbers(ingredient_list):
    # Prompt the user to select ingredients and validate input.
    selected_numbers = input("Enter the numbers of ingredients you'd like to search for, separated by spaces: ")
    selected_numbers = selected_numbers.split()

    # Validate the user's input
    if not all(num.isdigit() and 1 <= int(num) <= len(ingredient_list) for num in selected_numbers):
        print("Invalid input. Please enter valid numbers corresponding to the ingredients.")
        return []

    return selected_numbers


def search_recipes_by_ingredients(session, search_ingredients):
    # Search for recipes that match the selected ingredients.
    search_results = session.query(Recipe).filter(
        Recipe.ingredients.like(f"%{search_ingredients[0]}%")
    )

    for ingredient in search_ingredients[1:]:
        search_results = search_results.filter(Recipe.ingredients.like(f"%{ingredient}%"))

    return search_results.all()


def display_search_results(search_results):
    # Display the search results.
    if search_results:
        print("\nRecipes found:")
        for recipe in search_results:
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")


def edit_recipe(session):
    recipes = get_all_recipes(session)
    if not recipes:
        print("No recipes found in the database.")
        return

    selected_id = select_recipe(recipes)
    if selected_id is None:
        return

    recipe_to_edit = get_recipe_by_id(session, selected_id)
    display_recipe(recipe_to_edit)

    attribute_choice = select_editable_attribute()
    if attribute_choice is None:
        return

    update_recipe_attribute(recipe_to_edit, attribute_choice)
    recipe_to_edit.calculate_difficulty()

    session.commit()
    print("Recipe updated successfully!")
    print("Updated Recipe Details:")
    print(recipe_to_edit)


def select_recipe(recipes):
    # Display available recipes and prompt user to select one by ID.
    print("\nAvailable Recipes:")
    results = {recipe.id: recipe.name for recipe in recipes}
    for recipe_id, recipe_name in results.items():
        print(f"{recipe_id} - {recipe_name}")

    selected_id = input("Enter the ID of the recipe you'd like to edit: ")
    if not selected_id.isdigit() or int(selected_id) not in results:
        print("Invalid ID selected. Exiting edit function.")
        return None

    return int(selected_id)


def get_recipe_by_id(session, recipe_id):
    # Retrieve the recipe by given ID.
    return session.query(Recipe).filter_by(id=recipe_id).first()


def display_recipe(recipe):
    # "Display the details of the selected recipe.
    print("\nEditing Recipe:")
    print(recipe)


def select_editable_attribute():
    # Display editable attributes and prompt user to select one.
    print("What would you like to edit?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")

    attribute_choice = input("Enter the number of the attribute you'd like to edit: ")
    if attribute_choice in ['1', '2', '3']:
        return int(attribute_choice)
    else:
        print("Invalid choice. Exiting edit function.")
        return None
    

def update_recipe_attribute(recipe, attribute_choice):
    # Update the selected attribute of the recipe.
    if attribute_choice == 1:
        new_name = prompt_recipe_name()
        recipe.name = new_name
    elif attribute_choice == 2:
        new_ingredients = prompt_ingredients()
        recipe.ingredients = new_ingredients
    elif attribute_choice == 3:
        new_cooking_time = prompt_cooking_time()
        recipe.cooking_time = new_cooking_time


def delete_recipe(session):
    recipes = get_all_recipes(session)
    if not recipes:
        print("No recipes found in the database. Exiting delete function.")
        return

    print("\nAvailable Recipes:")
    for recipe in recipes:
        print(f"{recipe.id} - {recipe.name}")

    selected_id = input("Enter the number by the recipe you'd like to delete: ")
    if not selected_id.isdigit() or int(selected_id) not in {recipe.id for recipe in recipes}:
        print("Invalid number selected. Exiting delete function.")
        return

    recipe_to_delete = get_recipe_by_id(session, int(selected_id))
    
    confirm = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): ")
    if confirm.lower() == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Deletion canceled.")


def main():
    Base.metadata.create_all(engine)
    session = Session()

    while True:
        print("\nOptions: \n1. Add Recipe \n2. View All Recipes \n3. Search by Ingredients \n4. Edit Recipe \n5. Delete Recipe \n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_recipe(session)
        elif choice == '2':
            view_all_recipes(session)
        elif choice == '3':
            search_by_ingredients(session)
        elif choice == '4':
            edit_recipe(session)
        elif choice == '5':
            delete_recipe(session)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
    
        session.close()         

if __name__ == "__main__":
    main()
