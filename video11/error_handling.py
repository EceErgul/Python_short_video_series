# ERROR HANDLING

# Common Errors in Python

"""
ZeroDivisionError: dividing by 0
NameError: variable not defined
TypeError: combine incompatible types, like adding a number and a string.
ValueError: valid type but an inappropriate value, like converting "abc" to an integer.
"""

# Try - Except Blocks

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# Handling Multiple Exceptions

try:
    value = int(input("Enter a number: "))
    print(10 / value)
except (ZeroDivisionError, ValueError):
    print("Invalid input or division by zero!")

# Raising Exceptions

age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")

print(f"You are {age} years old.")

# Mini Practice

"""
- Take a password as input.
- Check if the password is at least 8 characters long.
- if shorter, raise a ValueError.
- Otherwise, print "Password accepted."
"""

password = input("Enter your password: ")

if len(password) < 8:
    raise ValueError("Password too short!")

print("Password accepted!")