import pickle

# recipe = {
#     'Name': 'Tea',
#     'Ingredients': ['Tea leaves', 'Water', 'Sugar'],
#     'Cooking Time': '5 minutes',
#     'Difficulty': 'Easy'
# }

# with open('recipe_binary.bin', 'wb') as recipe_file:
#     pickle.dump(recipe, recipe_file)


with open('recipe_binary.bin', 'rb') as recipe_file:
    loaded_recipe= pickle.load(recipe_file)

print("Vehicle details - ")
print("Name:  " + loaded_recipe['Name'])
# Check if Ingredients is a list and print accordingly
if isinstance(loaded_recipe['Ingredients'], list):
    print("Ingredients: ")
    for ingredient in loaded_recipe['Ingredients']:
        print("* " + ingredient)
else:
    print("Ingredients: " + loaded_recipe['Ingredients'])
print("Cooking Time: " + loaded_recipe['Cooking Time'])
print("Difficulty: " + loaded_recipe['Difficulty'])