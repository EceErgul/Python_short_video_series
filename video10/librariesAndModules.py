# Libraries and Modules

"""
-Modules are a collection of classes, functions, and variables that can be used in your code. 
    (math, random, etc.)
-Libraries are a collection of functions and variables that can be used in your code. 
    (numPy, pandas, etc.)
"""

# Importing Modules

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.sqrt(16))

# Creating Your Own Module

import video10.myModule as myModule

print(myModule.greet("Ece"))

# The Math Module

import math

print(math.sqrt(25))     # Square root
print(math.factorial(5)) # Factorial
print(math.pi)           # Value of pi

# Useful Libraries

import random
print(random.randint(1, 10))  # Random number between 1 and 10

import datetime
print(datetime.date.today())  # Today’s date

# Mini Practice

"""
- First, generate 5 random numbers between 1 and 100.
- Then,  calculate the square root of each of those numbers.
- Finally, print both the original numbers and their square roots side by side.
"""

"""
- First, generate 5 random numbers between 1 and 100.
- Then,  calculate the square root of each of those numbers.
- Finally, print both the original numbers and their square roots side by side.
"""

from random import randint
from math import sqrt

nums = [randint(1, 100) for _ in range(5)]
roots = [sqrt(n) for n in nums]

print("Numbers:", nums)
print("Square Roots:", roots)