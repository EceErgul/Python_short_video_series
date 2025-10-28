# LOOPS (While, For)

# While Loop

count = 1
while count <= 5:
    print("Counting:", count)
    count += 1

# For Loop

for i in range(5):
    print("Hello, world!")

for i in range(1, 6):
    print("Number:", i)

# Break Statement

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue Statement

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Mini Practice (Number guessing game)

"""
- if number is less than the secret number, print "Too low"
- if number is greater than the secret number, print "Too high"
- if number is equal to the secret number, print "You got it!"
- Start with: import random
- secret = random.randint(1, 10)
"""

# Solution
# random module (generates a random number)(Discussed in librariesAndModules)

import random

secret = random.randint(1, 10) # pick a random number between 1 and 10

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct! You guessed it!")
        break
    elif guess < secret:
        print("Too low. Try again.")
        continue
    else:
        print("Too high. Try again.")