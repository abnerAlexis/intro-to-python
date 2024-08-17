import pickle
import recipe_input

def display_recipe(recipe):
    print("Recipe Details:")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}\n")

def get_data(file):
    data = recipe_input.load_data(file)
    return data

def search_ingredient(data):
    all_ingredients = data.get('all_ingredients', [])
    
    print("Available Ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index + 1}. {ingredient}")

    try:
        choice = int(input("\nSelect the number corresponding to the ingredient you want to search for: ")) - 1
        ingredient_searched = all_ingredients[choice]
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"\nSearching for recipes containing: {ingredient_searched}\n")
        recipes_list = data.get('recipes_list', [])
        found_recipes = [recipe for recipe in recipes_list if ingredient_searched in recipe['ingredients']]

        if found_recipes:
            for recipe in found_recipes:
                display_recipe(recipe)
        else:
            print(f"No recipes found containing {ingredient_searched}.")

def main():
    filename = recipe_input.prompt_filename()
    data = get_data(filename)
    if data:
        search_ingredient(data)

if __name__ == "__main__":
    main()
