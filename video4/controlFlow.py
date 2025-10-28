# CONTROL FLOW

# Reminder of comparison operators
# ==, !=, <, >, <=, >=

# If Statement

age = 20

if age > 18:
    print("You are an adult")

# If-Else Statement

age1 = 16

if age1 >= 18:
    print("You are an adult")
else:
    print("You are under 18")

# If-Elif-Else Statement

Age = 16

if Age >= 18:
    print("You are an adult")
elif Age >= 13:
    print("You are a teenager")
else:
    print("You are under 18")

# Logical Operators (and, or, not)
#and
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert")
else:
    print("You cannot enter the concert")

#or
age = 15
parent_permission = False

if age >=18 or parent_permission:
    print("You can join the trip")
else:
    print("You cannot join the trip")

#not

age = 15

if not (13 <= age < 18):
    print("You are NOT a teenager.")
else:
    print("You ARE a teenager.")

# Mini Practice
"""
if 18 or older, can watch the movie
if 13 to 17, can watch the movie with parents
if under 13, cannot watch the movie
"""

# Solution

age = int(input("Enter your age: "))
has_parent =input("Are you a parent? (yes/no): ")

if age >= 18:
    print("You can watch the movie")
elif age >=13 and has_parent == "yes":
    print("You can watch the movie with parents")
else:
    print("Sorry, you ""cannot watch the movie")