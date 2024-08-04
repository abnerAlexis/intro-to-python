import json
import pprint

all_recipes = {
    'recipe_1' : {'name':'Tea', 'cooking_time': '5 minutes', 'ingredients': ['Tea leaves', 'Sugar', 'Water']},
    'recipe_2' : {'name':'Flex Seed Muffin', 'cooking_time': '90 seconds', 'ingredients': ['1 tbsp Flexs seeds', '1 tsp Honey', '1 Egg', '1/2 tsp baking soda']},
    'recipe_3' : {'name':'Pizza', 'cooking_time': '30 minutes', 'ingredients': ['Pizza dough', 'Tomato sauce', 'Cheese', 'Mushrooms', 'Sausage']},
    'recipe_4' : {'name':'Pasta', 'cooking_time': '11 minutes', 'ingredients': ['Pasta', 'Marinara', 'Meat']},
    'recipe_5' : {'name':'Egg Salad', 'cooking_time': '5 minutes', 'ingredients': ['Eggs', 'Green salad', 'Scallions', 'Olive oil', 'Lemon juice', 'Himalayan salt']}
}

for key, value in all_recipes.items():
    print(f"Ingredients for {value['name']}: {value['ingredients']}")

# Add another recipe to all_recipes
all_recipes['recipe_6'] = {
    'name': 'Brownies',
    'cooking_time': '25 minutes',
    'ingredients': ['Butter', 'Sugar', 'Eggs', 'Vanilla extract', 'Cocoa powder', 'Flour', 'Salt']
}

#pprint.pprint(all_recipes)     #Order of items change when using this.

# Pretty print with JSON to maintain order
print(json.dumps(all_recipes, indent=4))
