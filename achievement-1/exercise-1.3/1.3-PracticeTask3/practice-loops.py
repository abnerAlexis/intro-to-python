# for loop
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)
print("And we're done!")

# while loop
i = 0
while(i < len(numbers)):
    print(numbers[i])
    i += 1
print("And we're done!")

# populating a list using for loop
nums = []

for i in range(0, 21):
    nums.append(i)
print(nums)

# if used in loop
evens = []

for number in range(0, 30):
    if (number % 2 == 0 and number != 0):
        evens.append(number)
print(evens)

# enumaration
fruits = ['Apples', 'Oranges', 'Bananas']
for position, value in enumerate(fruits):
    print('item ' + str(position) + ': ' + value)

# out put will be a list of tuples - output [(0, 'Apples'), (1, 'Oranges'), (2, 'Bananas')]
list1 = list(enumerate(fruits))
print(list1)

# another example of enumaration - output [(100, 'Apples'), (101, 'Oranges'), (102, 'Bananas')]
list2 = list(enumerate(fruits, 100))
print(list2)