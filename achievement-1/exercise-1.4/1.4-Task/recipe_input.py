import pickle

recipes_list = []
ingredients_list = []

def main():
    recipes_list = populate_recipes_list()
    filename = prompt_filename()
    write_data(filename)
    load_data(filename)

# Adds recipe to the recipes_list
def populate_recipes_list():
    n = int(input("How many recipes would you like to enter? "))
    for _ in range(n):  # Underscore to indicate an unused loop variable
        recipe = take_recipe()
        recipes_list.append(recipe)
    return recipes_list

# Returns a single recipe as a dictionary
def take_recipe():
    name = input("\nEnter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = []

    print(
        "Type each ingredient and press Enter. When you've added all ingredients, press Enter again to confirm."
    )
    while True:
        ingredient = input("Ingredient: ")
        if not ingredient:
            break

        # ingredients belongs to one specific recipe
        ingredients.append(ingredient)

        # Adding the ingredient to ingreidents_list if it doesn't contain one already.
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": calc_difficulty(cooking_time, len(ingredients)),
    }
    # print(recipe)
    return recipe


def calc_difficulty(cook_time, ingredient_count):
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
# prompt user for filename   
def prompt_filename():
    filename = input("File Name: ")
    return filename

def load_data(filename):
    try:
        with open(filename, "rb") as data:
            data = pickle.load(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        data = None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        data = None

    return data

data = {'recipes_list': recipes_list,
        'all_ingredients': ingredients_list}
# print(data)

def write_data(filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except Exception as error:
        print(f"An error occurred while writing to the file: {error}")

if __name__ == "__main__":
    main()