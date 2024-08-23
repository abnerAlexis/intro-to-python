class Recipe:
    # Class variable to keep track of all ingredients across all recipes
    all_ingredients = set()

    def __init__(self, name, ingredients=None, cooking_time=0):
        self.name = name
        self.ingredients = ingredients if ingredients else []
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()  # Calculates difficulty after initialization
        self.update_all_ingredients()

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        # Update difficulty when cooking time changes
        self.difficulty = self.calculate_difficulty() 

    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        # Call to update all ingredients after adding new ones
        self.update_all_ingredients() 
    
    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)

        if self.cooking_time < 10 and num_ingredients < 4:
            return 'Easy'
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return 'Intermediate'
        else:
            return 'Hard'
        
    def get_difficulty(self):
        return self.difficulty
    
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            # Update the class variable with unique ingredients
            Recipe.all_ingredients.add(ingredient)
    
    def recipe_search(data, search_term):
        print(f"\nSearching the recipes with ingredient: {search_term}")
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe) #__str__ will be used to print
                found = True
        if not found:
            print(f"No recipe found with the ingredient {search_term}.")

    def __str__(self):
        output = f"\nRecipe: {self.name}\n"
        output += f"Ingredients: {', '.join(self.ingredients)}\n"
        output += f"Cooking Time: {self.cooking_time} minutes\n"
        output += f"Difficulty: {self.difficulty}"
        return output
    
def main():
    # Creating the Tea recipe
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)
    print(tea)

    # Creating the Coffee recipe
    coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
    print(coffee)

    # Creating the Cake recipe
    cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
    print(cake)

    # Creating the Banana Smoothie recipe
    banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
    print(banana_smoothie)

    # Wrapping recipes into a list
    recipes_list = [tea, coffee, cake, banana_smoothie]

    # Searching for recipes that contain specific ingredients
    Recipe.recipe_search(recipes_list, "Water")
    Recipe.recipe_search(recipes_list, "Sugar")
    Recipe.recipe_search(recipes_list, "Bananas")


if __name__ == "__main__":
    main()