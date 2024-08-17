divident = input("Divident: ")
divisor = input("Divisor: ")

try:
    result = float(divident) / float(divisor)
    # print(f"{divident} divided by {divisor} is {result:.2f}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
else:
    print(f"{divident} divided by {divisor} is {result:.2f}") # This is an option
finally:
    print("Process complete!")