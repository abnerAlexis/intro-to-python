recipes_list = []
ingredients_list = []

# Adds recipe to the recipes_list
def populate_recipes_list():
    n = int(input('How many recipes would you like to enter? '))
    for _ in range(n):  # Underscore to indicate an unused loop variable
        recipe = take_recipe()  
        recipes_list.append(recipe)
    print_all_recipes()    

# Returns a single recipe as a dictionary
def take_recipe():
    name = input('\nEnter the recipe name: ')
    cooking_time = int(input('Enter the cooking time in minutes: '))
    ingredients = []

    print("Type each ingredient and press Enter. When you've added all ingredients, press Enter again to confirm.")
    while True:
       ingredient = input("Ingredient: ")
       if not ingredient: 
          break
       
       # ingredients belongs to one specific recipe
       ingredients.append(ingredient)

       # Adding the ingredient to ingreidents_list if it doesn't contain one already.
       if ingredient not in ingredients_list:
        ingredients_list.append(ingredient)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    # print(recipe)
    return recipe

# Determine difficulty based on ingredient count and cooking time
def determine_difficulty(ingredient_count, cook_time):
   if cook_time < 10 and ingredient_count < 4:
      return 'Easy'
   elif cook_time < 10 and ingredient_count >= 4:
      return 'Medium'
   elif cook_time >= 10 and ingredient_count < 4:
      return 'Intermediate'
   elif cook_time >= 10 and ingredient_count >= 4:
      return 'Hard'
   else: 
      return 'Unknown'

def print_recipe(recipe=None):
    recipe = recipe or take_recipe()
    # Extract details from the recipe
    name = recipe.get('name')
    cooking_time = recipe.get('cooking_time')
    ingredients = recipe.get('ingredients', [])
    ingredient_count = len(ingredients)
    
    for key, value in recipe.items():
        # Customizing the key labels
        if key == 'name':
            display_key = '\nRecipe'
        elif key == 'cooking_time':
            display_key = 'Cooking Time (min)'
        elif key == 'ingredients':
            display_key = 'Ingredients'
        else:
            display_key = key.replace('_', ' ').capitalize()
        
        # Handling list printing
        if isinstance(value, list):
            print(f"{display_key}:")
            for item in value:
                print(f"{item.capitalize()}")
        else:
            print(f"{display_key}: {value}")

    # Add difficulty to the print output
    difficulty = determine_difficulty(ingredient_count, cooking_time)
    print(f"Difficulty level: {difficulty}")

def print_all_recipes():
    print("\nAll Recipes:")
    for recipe in recipes_list:
        print_recipe(recipe)  # Print each recipe using the print_recipe method

def print_all_ingredients():
  print('\nIngredients Available Accross All Recipes:')
  ingredients_list.sort()
  for ingredient in ingredients_list:
    print(ingredient.capitalize())

populate_recipes_list()
print_all_ingredients()