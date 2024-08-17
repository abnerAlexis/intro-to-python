numbers = []
for i in range(50, 101):
    numbers.append(i)
print(numbers)

with open('number_list.txt', 'w') as num_files:
    num_files.writelines(str(number) + '\n' for number in numbers)

#   there’s no need to close the file! The with keyword already takes care of that