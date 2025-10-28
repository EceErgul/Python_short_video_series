# FUNCTIONS

# Defining a function

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# Return values & Scopes

def square(num):
    return num, num ** 2

value, result = square(5)
print("square of", value, "is: ", result)

x = 10  # global variable
def add_to_x(num):
    return x + num  # can access global variable

print(add_to_x(5))

# Default & keyword arguments

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")
greet(name="Bob")

# Lambda Functions

square = lambda x: x ** 2
print(square(5))

# filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# map() function
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Mini Practice

"""
- You have a list of words: ["apple", "banana", "cherry", "date", "elderberry"].
- Use map() with a lambda function to get the length of each word.
- Use filter() with a lambda function to keep only words longer than 5 characters.
"""

words = ["apple", "banana", "cherry", "date", "elderberry"]

# Use map with lambda to get lengths
lengths = list(map(lambda w: len(w), words))
print("Word lengths:", lengths)

# Use filter with lambda to keep words longer than 5 characters
long_words = list(filter(lambda w: len(w) > 5, words))
print("Words longer than 5 characters:", long_words)