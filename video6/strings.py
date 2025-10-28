# STRINGS

sentence = 'Python is fun!'
name = "Ece"
multi_line = """This is
a multi-line
string."""

# String Indexing

"""  P    y    t    h    o    n
    [0]  [1]  [2]  [3]  [4]  [5]
   [-6] [-5] [-4]  [-3] [-2] [-1]
"""
word = "Python"
print(word[0])   # First character: 'P'
print(word[1])   # Second character: 'y'
print(word[-1])  # Last character: 'n'
print(word[-2])  # Second last: 'o'

# Common string methods

text = "  hello world  "

print(len(text))           # Length of string: counts all characters including spaces
print(text.upper())        # 'HELLO WORLD' - converts to uppercase
print(text.lower())        # 'hello world' - converts to lowercase
print(text.strip())        # removes leading/trailing spaces: 'hello world'
print(text.replace("world", "Python"))  # '  hello Python  '
print(text.startswith("  h"))           # True - checks prefix
print(text.endswith("ld  "))            # True - checks suffix
print(text.count("l"))      # counts occurrences of 'l'
print(text.find("world"))   # returns starting index of substring or -1 if not found

# String formatting

# f-string

name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")

print(f"Two plus two is {2+2}.")

# format

print("My name is {} and I am {} years old.".format(name, age))
# format using indexes
print("I am {1} years old and my name is {0}.".format(name, age))
# #formatting numbers
pi = 3.14159
print(f"Pi rounded to 2 decimal places is {pi:.2f}")

# Slicing & Advanced string manipulation

word = "Python"
print(word[0:4])   # 'Pyth' - from index 0 to 3 (end is exclusive)
print(word[:4])    # 'Pyth' - start defaults to 0
print(word[2:])    # 'thon' - goes till the end
print(word[::2])   # 'Pto'  - skips every 2nd char
print(word[::-1])  # 'nohtyP' - reverses the string

# Mini Practice

"""
-Take a user's name as input.
-Remove any extra spaces at the start and end.
-Print the name in uppercase.
-Print only the first three letters of the name.
-Show the length of the cleaned name.
"""

# Solution

name = input("Enter your name: ")

clean_name = name.strip()
print(f"Uppercase: {clean_name.upper()}")
print(f"First three letters: {clean_name[:3]}")
print("Length: {}".format(len(clean_name)))