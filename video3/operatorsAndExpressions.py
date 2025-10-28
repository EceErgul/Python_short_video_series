# OPERATORS

print(3 + 4)
print(10 - 2)
print(4 * 5)

# +, -, * are arithmetic operators

# Arithmetic operators

print(10 / 3)    # division (returns float)
print(10 // 3)    # floor division (cuts off the decimal)
print( 10 % 3)    # modulus (returns the remainder)
print(2 * 3)    # multiplication (returns the product)
print(2 ** 3)    # exponentiation (power of)

# Comparison operators

# > (greater than),  == (equal to), < (less than),  != (not equal to),
# >= (greater than or equal to),  <= (less than or equal to)

print(5 > 3)
print(3 <= -4)
print(5 == 5)
print(5 != 2)
print(4 >= 4)
print(2 < 1)

# Logical operators

# and, or, not
# print(5 > 3 and 4 > 2)
# print(3 > 5 or 1 < 4)
# print(not True)

# Operators precedence

print(3 + 2 * 4) # multiplication has higher precedence than addition
print((3 + 2) * 4) # parentheses can be used to change precedence

# Mini Practice - Splitting the Bill equally to 3 people
"""
 - Start with a bill of $45
 - Add a 10% tip to the bill
 - Split the total equally to 3 people
"""

# Solution

bill = 45
tip = bill * 0.10
total = bill + tip
per_person = total / 3
print("Each person should pay:", per_person)

perPerson = (45 + 45 * 0.10) / 3
print("Each person should pay (using variable):", perPerson)