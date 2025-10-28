# LISTS AND TUPLES

# Lists

fruits = ["apple", "banana", "cherry"]
# Indexes:  [0]  ,   [1]   ,   [2]
print(fruits)

fruits[1] = "blueberry"
print(fruits)

# List Methods

print(f"Original list: {fruits}")

fruits.append("orange") #append() - add at the end
print(f"After append: {fruits}")

fruits.insert(1, "blueberry") #insert() - add at specific position
print(f"After insert: {fruits}")

fruits.remove("banana") #remove() - remove first occurrence of an item
print(f"After remove: {fruits}")

last_item = fruits.pop() #pop() - remove by index (default last item)
print(f"After pop: {fruits}, popped item: {last_item}")

fruits.sort(reverse = True) #sort() - sort the list alphabetically
print(f"After sort: {fruits}")

fruits.reverse() #reverse() - reverse the list
print(f"After reverse: {fruits}")

fruits.append("apple") #count() - count occurrences of a value
print(f"Count of 'apple': {fruits.count('apple')}")

print(f"Index of 'cherry': {fruits.index('cherry')}") #index() - find first index of a value

fruits_copy = fruits.copy() #copy() - create a shallow copy
print(f"Copied list: {fruits_copy}")

fruits.clear() #clear() - remove all items
print(f"After clear: {fruits}")

# Tuples

coordinates = (10, 20)
print(coordinates)

coordinates[1] = 30 # This will raise an error because tuples are immutable
print(coordinates)

# Iterating in lists and tuples

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
print()

coordinates = ((10,20),(30.0,10),(95.5,4))
for coordinate in coordinates:
    print(coordinate)

# Mini Practice

"""
-Create a collection of your favorite movies (or books, foods, anything you like).
-Decide whether it makes more sense to use a list or a tuple.
-Think about how you would add, remove, or organize items if needed.
-Use a loop to print each item nicely.
"""

# Solution

favorites = ["Inception", "The Matrix", "Interstellar"]

favorites.append("The Dark Knight")
favorites.remove("The Matrix")
favorites.sort()

for movie in favorites:
    print(f"- {movie}")