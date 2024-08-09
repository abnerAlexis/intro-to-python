print('Comparison operators : <, >, <=, >=, ==, and !=')
a, b = 1, 2
print('a is less than b:', a < b)
print('a equals to b:', a == b)
print('a is not equal to b:', a != b)
print('a is less or equal to b:', a <= b)

a, b, c = 1, 2, 3
print('a is less than b less than c:', a < b < c)

age = int(input("Enter your age: "))
print("Age between 18 and 35: " + str(18 < age < 35))