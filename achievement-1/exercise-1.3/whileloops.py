number = 5

while number < 11:
    print(number)
    number = number + 1

#The break and continue Statements
num = int(input("Enter a number to be divided: "))
start = int(input("Enter a starting point for the divisor: "))
end = int(input("Enter an end point for the divisor: "))

for div in range(start, end):
    if div == 0:
        print("Division by zero, exiting.")
        break
    print(num / div)

num = int(input("Enter a number to be divided: "))
start = int(input("Enter a starting point for the divisor: "))
end = int(input("Enter an end point for the divisor: "))

for div in range(start, end):
    if div == 0:
        print("Division by zero, skipping to next value.")
        continue
    print(num / div)