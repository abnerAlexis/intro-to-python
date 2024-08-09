def add(a, b):
    result = a + b
    print("The added result is " + str(result))

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
add(a, b)

# Calling Functions with Keyword Arguments
def divide(value_1, value_2):
    print('Division result:', str(value_1 / value_2))

a = int(input('First number:'))
b = int(input('Second number:'))

#All below return 4.0
divide(a, b)
divide(value_1=a, value_2=b)
divide(value_2=b, value_1=a)

# Defining Functions with Default Arguments
def price_tag(product_name='No name specified.', price=0):
    print('Product: ' + product_name)
    print('Price: $' + str(price))
price_tag('IPhone 15 Pro', 1000)    # returns Product: IPhone 15 Pro   Price: $1000
price_tag('IPhone 7')               # returns Product: IPhone 7   Price: $0
price_tag()                         # returns Product: No name specified. Price: $0

# Passing Variable-Length Arguments into Functions
def tech_brands(*brands):
    for brand in brands:
        print(brand + ' ', end='')

tech_brands('Apple', 'Samsung', 'SpaceX')   # tech_brands accepts any number of arguments as a sequence called brands
# output Apple Samsung SpaceX
print('\n')

# Returning Values from Functions
def my_func(a, b):
    print("Returning 'a'!")
    return a

val = my_func(3, 5)
print(val)

# Using the global Keyword
text = "I like apples"

def my_func():
    global text
    # We'll try joining another string to 'text'
    text = text + "... but I love oranges better!"
    print("text from the inside: " + text)

my_func()
print("text from the outside: " + text)