# vegetables = ['Carrot', 'Tomato', 'Asparagus', 'Spinach', 'Kale']
# veggy_file = open('vegetables.txt', 'w')
# veggy_file.writelines(vegetables)
# veggy_file.close()

# vegetables = ['Carrot\n', 'Tomato\n', 'Asparagus\n', 'Spinach\n', 'Kale\n']
# veggy_file = open('vegetables.txt', 'w')
# veggy_file.writelines(vegetables)
# veggy_file.close()

vegetables = ['Carrot', 'Tomato', 'Asparagus', 'Spinach', 'Kale']

with open('vegetables.txt', 'w') as veggy_file:
    veggy_file.writelines([vegetable + '\n' for vegetable in vegetables])