desserts_file = open('desserts.txt', 'r')
print(desserts_file.read(10)) # Blueberry
print('file.tell():', desserts_file.tell()) # 10
print('file.seek():', desserts_file.seek(0)) # reset -f in terminal for ipython

string_complete = desserts_file.read()
print(string_complete)
print('file.tell():', desserts_file.tell()) #138
print('file.seek():', desserts_file.seek(0))

all_desserts = desserts_file.readlines() # ['Blueberry Cheesecake\n', 'Ice Cream\n', 'Churros\n', 'Crème Brûlée\n', 'Chocolate Mousse Cake\n', 'German Chocolate Cake\n', 'Jell-O\n', 'Carrot Cake\n', 'Tiramisu\n', 'Marble Cake']
print(all_desserts) # will print \n newline syntax too - rstrip every dessert

all_desserts_stripped = []
for dessert in all_desserts:
    all_desserts_stripped.append(dessert.rstrip('\n'))
print(all_desserts_stripped) # ['Blueberry Cheesecake', 'Ice Cream', 'Churros', 'Crème Brûlée', 'Chocolate Mousse Cake', 'German Chocolate Cake', 'Jell-O', 'Carrot Cake', 'Tiramisu', 'Marble Cake']

# Closing the file stream
desserts_file.close()