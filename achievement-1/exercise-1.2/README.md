# Tuples
Tuples are linear arrays. Series of values can be stored with tuples with their given meaningful names to them. Tuples can contain objects, numbers, strings and more. They are immutable

## Tuple syntax
Tuple syntax in Python involves creating an immutable, ordered collection of items enclosed in parentheses, with elements separated by commas. e.g `tupl = (1, 2, 3)`

## Tuples are immutable
This means they can't be altered. There are workarounds to make alterations. e.g. to add an element to a tuple.
```
t = (2, 5, 7)
a = ('Tea', 2, 'Chocolate')
t = t + a

print(t) # This will return (2, 5, 7, 'Tea', 2, 'Chocolate')

t = t * 2
print(t) # This will return (2, 5, 7, 'Tea', 2, 'Chocolate', 2, 5, 7, 'Tea', 2, 'Chocolate')

```
## Slicing

Slicing is extracting a subset of elements from the original tuple.

```

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
```

| Print Statement                             | Return                                                  |
|---------------------------------------------|--------------------------------------------------------------|
| `print("Full tuple:", my_tuple)`            | Output the entire tuple                                     |
| `print("Slice from index 2 to 5:", my_tuple[2:6])` | Elements from index 2 to 5 (30, 40, 50, 60)              |
| `print("Slice from the start to index 4:", my_tuple[:5])` | Elements from the start to index 4 (10, 20, 30, 40, 50) |
| `print("Slice from index 3 to the end:", my_tuple[3:])` | Elements from index 3 to the end (40, 50, 60, 70, 80, 90)|
| `print("Slice with step 2:", my_tuple[::2])` | Every second element (10, 30, 50, 70, 90)                  |
| `print("Slice with step -1 (reversed):", my_tuple[::-1])` | The tuple reversed (90, 80, 70, 60, 50, 40, 30, 20, 10)  |


## Positive and Negative indexes

In Python, positive indexes count from the beginning of a sequence, starting at 0 for the first element.  
Negative indexes count from the end of a sequence, starting at -1 for the last element. 

| Positive Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|----------------|---|---|---|---|---|---|---|---|
| Sequence       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Negative Index | -8| -7| -6| -5| -4| -3| -2| -1|

## max() and min() functions
The max() returns the largest item in a tuple. 
The min() returns the smallest item in a tuple.

e.g.
```
max((1, 'a', 3))  # This will raise a TypeError
min((1, 'a', 3))  # This will raise a TypeError  

max((1, 3, 2))    # This will return 3
min((1, 3, 2))    # This will return 1  

max(('a', 'b', 'c'))  # This will return 'c'
min(('a', 'b', 'c'))  # This will return 'a'

```

## count() function
count() function returns the number of occurrances of a querried element in a tuple. e.g.  
```
tpl = (4, 7, 4, 9, 7, 4, 5, 9, 5, 7)
print(tpl.count(4))     # This will return 3

```

## <span style="color: lightblue;">in</span> keyword
The `in` keyword in Python is used to check if a value exists within a tuple, returning True if the value is found and False otherwise.

## index() function
Returns the index number of a specified element. If there are more than one occurance of that element, it will return the index number of the first occurance.
```
abc = ('a', 'b', 'c', 'b')
print(abc.index('b')) # This will return 1

```

# Lists
A list in Python is an ordered, mutable sequence that allows for changes, additions, and removals of elements. Unlike tuples, which are immutable and cannot be altered after creation.

## List syntax
A List has a sequence of values between square brackets `[ ]`
With lists, printing, indexing, and slicing are similar to tuples, and both support iteration, concatenation, and repetition. Additionally, functions like max(), min(), and count() work the same way as they do with tuples. Like tuples, lists use zero-based indexing, allow nested structures (lists within lists or tuples), and can be accessed using negative indexing.

###### Declaring a list:
```
lst = [1, 2.5, 'hello', True]

```

## Modifying Elements in a List
The syntax to modify an element in a list is:

```
<list name>[element position] = <new value>

```

## Changing elements of a list

```
 lst = [1, 2.5, 'hello', True]
 lst[2] = 'orange'
 print(lst)  # This will print [1, 2.5, 'orange', True]
 ```

 ## Adding New Elements Into a List
 ### append()
 ```
 lst.append(826)
 print(lst)  # This will print [1, 2.5, 'orange', True, 826]
 ```
 ### extend()
 With extend(), you can add several items at once.
 ```
 severalItems = [7, 'Fox', 'Wednesday']
 lst.extend(severalItems)
 print(lst) # This will print [1, 2.5, 'orange', True, 826, 7, 'Fox', 'Wednesday']
 ```
 ### + operator
 ```
 list1 = [1, 2, 3]
 list2 = [4, 5, 6]
 combined_list = list1 + list2

 print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
 ```
 ### inserting items into a specific index
 The insert() function in Python lists allows you to add an element at a specified index, shifting subsequent elements to the right, with the syntax `list.insert(index, element)`.
 ```
# Original list
my_list = [1, 2, 4, 5]

# Insert 3 at index 2
my_list.insert(2, 3)
print(my_list)  # This returns [1, 2, 3, 4, 5]
```

### remove(), pop() and clear()
The remove() method in Python lists is used to delete the first occurrence of a specified value, raising a ValueError if the value is not found. The pop() method, on the other hand, removes and returns an element from the list at a specified index (defaulting to the last element if no index is provided), raising an IndexError if the list is empty or the index is out of range. Both methods modify the list in place.

alist = [0, 1, 2, 3]alist.remove(2)
print(alist)  # Output: [0, 1, 3]

 alist = [0, 1, 2, 3] | function use | print
|----------------|---|---|
| remove()  | alist.remove(2) | print(alist)  # Output: [0, 1, 3] | 
| pop()  | alist.pop(1) | print(alist)           # Output: [0, 2] | 
| clear()  | alist.clear() | print(alist)           # Output: [] | 

## Aliasing

For regular variables like a float, copying values from one variable to another is done with the = assignment operator, and the variables will then be independent of each other.
```
a = 3.14
b = a
b = b * 2
print(a, b)     This will return    3.14 6.28
```
But if you have list a and assign it the name `b`, the original list `a` will still exist. `b` acts as an “alias” for the original list, pointing to the same location in the memory where the original list is stored. This means that when you make changes in `b`, they’ll be made in `a` as well. e.e.
```
a = [1, 2, 3, 4, 5]
b = a
b[2] = 30
print(a)    this will return    [1, 2, 30, 4, 5]
```

### copy()
To make changes to a copy of your list without affecting the original, you need to use the copy() function. It works like this:
```
a = [1, 2, 3, 4, 5]
b = a.copy()
b[2] = 30
print(a)
[1, 2, 3, 4, 5]    # The original list is unaffected
```
## sort() and reverse()
The sort() method sorts the elements of a list in ascending order.
```
alist.sort()
print(alist)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
```

The reverse() method reverses the elements of the list in place.
```
alist = [3, 1, 4, 1, 5, 9, 2, 6, 5]
alist.reverse()
print(alist)  # Output: [5, 6, 2, 9, 5, 1, 4, 1, 3]
```
# Strings
Strings are sequences of characters used to represent text. They are defined by enclosing characters within either single quotes (') or double quotes (").  
Strings are immutable, meaning you can't change individual characters. To modify a string, you create a new string.
```
greeting = "Hello, world!"
name = 'Joe'
```
You can access individual characters using indexing (starts from 0):
```
print(greeting[0])  # Output: H
```
To find the length of a string, use len():
```length = len(greeting)
print(length)  # Output: 13
```
You can extract a substring using slicing:
```
substring = greeting[7:12]  # Output: world
```
Combine strings using the `+` operator:
```
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, world!, Alice!
```
### Common String Methods
`upper()`: Converts to uppercase  
`lower()`: Converts to lowercase  
`strip()`: Removes whitespace from the beginning and end  
`split()`: Splits a string into a list of words  
`replace()`: Replaces occurrences of one substring with another  
`find()`: Returns the index of the first occurrence of a substring  
```
text = "  This is a sample text  "
print(text.upper())  # Output:   THIS IS A SAMPLE TEXT  
print(text.strip())  # Output: This is a sample text
print(text.split())  # Output: ['This', 'is', 'a', 'sample', 'text']
```
### Negative Indexing
```
my_string = "hello"
print(my_string[-1])  # Output: o
print(my_string[-3])  # Output: l

my_string = "hello world"
print(my_string[2:-2])  # Output: llo wor
```

### Reversing a String with Slicing
```
my_string = "hello"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: olleh
```
# Dictionaries
Dictionaries are a data structure that store data in key-value pairs.
## syntax
Curly braces `{}` define a dictionary.
Each key-value pair is separated by a colon `:`.
`my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}`  

Use square brackets `[]` with the `key` to access the corresponding value.  
`my_dict['name']` or `my_dict.get('name')`  

You can set a default value to be returned if the key doesn’t exist instead of None  
`print(my_dict.get('lastname', 'lastname doesn't exist.'))`  

## Setting and Updating
Creating a new key
```
my_dict['lastname'] = 'Blue'
```
Updating an existing score
```
my_dict['age'] += 1    
```
Printing a dictionary
```
print(my_dict) 
```
### Deleting Key-Value Pairs  pop() 
The pop() method removes a key-value pair and returns the value associated with the key.
```
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
removed_value = my_dict.pop('age')
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}
print(removed_value)  # Output: 30
```
You can also provide a default value to return if the key is not found:
```
value = my_dict.pop('country', 'Unknown')  # Key 'country' doesn't exist
print(value)  # Output: Unknown
```
### Deleting all items
To remove all items from a dictionary, use the clear() method:
```
my_dict.clear()
print(my_dict)  # Output: {}
```

# Other Useful Dictionary Operations
## keys()
The keys() method returns a view object containing all the keys in the dictionary. 
```
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])
```
## values()
The values() method returns a view object containing all the values in the dictionary.  
```
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 30, 'New York'])
```
## items()
The items() method returns a view object containing the key-value pairs as tuples. 
```
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])```
```
## Explicit Type Conversion
Aso known as type casting, is when you manually convert a value from one data type to another.  
### Examples of explicit type conversion involving dictionaries
Converting a list of tuples to a dictionary:
```
list_of_tuples = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
dictionary = dict(list_of_tuples)
print(dictionary)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
Converting two lists to a dictionary:  
```
keys = ['key1', 'key2', 'key3']
values = ['value1', 'value2', 'value3']
dictionary = dict(zip(keys, values))
print(dictionary)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
Converting a dictionary to a list of keys:
```
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
keys_list = list(dictionary.keys())
print(keys_list)  # Output: ['key1', 'key2', 'key3']
```
Converting a dictionary to a list of values:
```
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
values_list = list(dictionary.values())
print(values_list)  # Output: ['value1', 'value2', 'value3']
```
Converting a dictionary to a list of key-value pairs (tuples):  
```
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
items_list = list(dictionary.items())
print(items_list)  # Output: [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
```
Creating a dictionary from two lists using a dictionary comprehension:  
```
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3}
```