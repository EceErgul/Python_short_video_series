# File Handling

# Open a File

myFile = open("sample.txt", "r") # mode: read(r), write(w), append(a)

#reading a file

content = myFile.read()
# read() -> entire file content, readline() -> line by line, readlines() -> list of lines
print("file content: ",content)

# closing the file

myFile.close()

# opening a file using with statement

with open("sample.txt", "r") as myFile:
    content = myFile.read()
    print("file content: ",content)

# writing to a file

with open("notes.txt", "w") as f:
    f.write("Hello, world!")

# appending to a file

with open("notes.txt", "a") as f:
    f.write("\nGoodbye, world!")

with open("notes.txt", "r") as f:
    content = f.read()
    print("file content: \n ",content)

# Working with JSON
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

person = {"name": "Alice", "age": 25, "city": "Ankara"}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Mini Practice

"""
 - Create a Python dictionary with some information about a student — like
        their name, age, and a list of grades.
 - Save this dictionary into a JSON file.
 - Then, read the JSON file back into Python and print the data to make sure it was saved correctly
"""

import json

student = {
    "name": "Ece",
    "age": 20,
    "grades": [85, 90, 92]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)