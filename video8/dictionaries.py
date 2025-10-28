# DICTIONARIES

# Dictionary with multiple values per key

student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Python", "Data Science"]
}
print("All courses: ", student["courses"])         # Prints the whole list
print("Second course: ", student["courses"][1])      # Prints 'Python'

# Dictionary Methods

print(student.keys())      # Returns all keys
print(student.values())    # Returns all values (including lists)
print(student.items())     # Returns key-value pairs
student["age"] = 22        # Update a value
student["GPA"] = 3.7       # Add a new key-value pair
student["courses"].append("AI")  # Add a course to the list
student.pop("GPA")         # Removes 'GPA'
print(student)

# Dictionary Comprehensions

# Squares of numbers
squares = {x: x**2 for x in range(1, 6)}
print("first example: ",squares)

# Transforming values of an existing dictionary
grades = {"Alice": 80, "Bob": 70, "Charlie": 90}
adjusted = {student: score + 5 for student, score in grades.items()}
print("second example: ",adjusted)

# Filtering items
numbers = range(10)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print("last example: ",even_squares)

# When to use Dictionary vs List

# Use a LIST when you just need values in order.
fruits = ["apple", "banana", "Cherry"]
# Use a DICTIONARY when you need labels (keys) or when values might themselves be collections.
fruitPrices = {"apple": 1.5, "banana": 0.75, "Cherry": 2.0}

# Mini Practice

"""
-Start with a list of words
-Create a dictionary using dictionary comprehension where each word maps to its length.
-Create a new dictionary that filters out words with 4 or fewer letters.
"""

words = ["apple", "dog", "banana", "cat", "elephant"]

# Dictionary with word lengths
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# Dictionary with words longer than 4 letters
long_words = {word: length for word, length in word_lengths.items() if length > 4}
print("Long words only:", long_words)
