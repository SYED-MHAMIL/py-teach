# Key Points:
# Operands are the "inputs" for an operator.
# The number of operands depends on the operator:
# Unary operators (e.g., not, -) work with one operand.
# Binary operators (e.g., +, -, *, /) work with two operands.
# Unary Operators
# Unary operators work with one operand (a single value or variable). They perform operations on just one thing.



# Examples:
# Negative (-):
# Changes the sign of the operand.

x = 5
y = -x  # y is now -5
# print("y = ", y)
     
y =  -5
# Logical NOT (not):
# Reverses a boolean value.

a = True
b = not a  # b is now False
# print("b = ", b)





# Bitwise NOT (~):
# Inverts the bits of a number (used in binary operations).
     


x: int = 5  # Binary: 0101
y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
# print("y = ", y)

# You can print an integer as a binary number in Python using the bin() function. Here's an example:

# The binary string is prefixed with '0b' to indicate that it's a binary number.

# print(x)
# print("bin(x) = ",bin(x), type(bin(x)))
# bin(x) =  0b101 <class 'str'>

num: int = x
# print(format(num, 'b'))  # Output: 1010
# print(f"{num:b}")  # Output: 1010
     
# 101
# 101

c = 4556
# print(bin(c))
# print(f"{c:b}")





# Key Difference:
# Unary Operators: Work with one operand (e.g., -x, not a).
# Binary Operators: Work with two operands (e.g., a + b, x > y).
# Operators in Python
# Operators in Python are symbols used to perform operations on variables and values. Python supports several types of operators:

# 1. Arithmetic Operators


# x: int = 10
# y: int = 5

# print("x == y = ", x == y)  # False, Equal
# print("x != y = ", x != y)  # True, Not equal
# print("x > y  = ", x > y)   # True, Greater than
# print("x < y  = ", x < y)   # False, Less than
# print("x >= y = ", x >= y)  # True, Greater than or equal
# print("x <= y = ", x <= y)  # False, Less than or equal
     




#     3. Logical Operators
# Used to combine conditional statements.

# Operator	Name	Example
# and	  Logical AND	(5 > 3 and 10 > 5) → True
# or	  Logical OR	(5 > 3 or 10 < 5) → True
# not	   1Logical NOT	not(5 > 3) → False



# 5. Identity Operators
# Used to compare memory locations.


# a: list = [1, 2, 3]
# b: list = [1, 2, 3]
# c: list = a

# print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
# print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
# print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
# print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)





# Excellent question! Python automatically interns (caches) certain immutable objects to improve performance and memory efficiency. Here's a breakdown:




# d = 1000
# de = 1000
# # if same value in integer so python trat them in one memory location
# print(d is de)







# x = "hello world! sdsdsd ada asdjasdasjdas asdasjkdasdasjdlasdjaskldasdasdasldjaskldjasldkjasdklasjdlasdjaskldjasld asdkasldasjdlaskdj aslkdja $$$44@#$@#$@#$@#@#@ @# fsdifsdoih if  sd fsd  0e8e083302482304249238423084 ?/"
# y = "hello world! sdsdsd ada asdjasdasjdas asdasjkdasdasjdlasdjaskldasdasdasldjaskldjasldkjasdklasjdlasdjaskldjasld asdkasldasjdlaskdj aslkdja $$$44@#$@#$@#$@#@#@ @# fsdifsdoih if  sd fsd  0e8e083302482304249238423084 ?/"
# print(x is y)

# a = "this_is_a_very_long_string_with_special_characters!@#%$&*()_+"
# b = "this_is_a_very_long_string_with_special_characters!@#%$&*()_+"

# print(a == b)   # ✅ True → content is same
# print(a is b)   # ❌ False → not the same object (not interned)



# d="1000 is"
# de="1000 is"

# print(d is de)

# a = "1000"
# b = "".join(["1", "000"])
# print(a == b)  # ✅ True (same value)
# print(a is b)  # ❌ False (different memory, not interned)





# ✅ 3. Booleans and None:
# These are singleton objects, always interned.



# x = True
# y = True
# print(x is y)  # ✅ True

# a = None
# b = None
# print(a is b)  # ✅ 



# 🚫 Not Interned:
# Floats
# Lists
# Dictionaries
# Sets
# Custom objects



# s1 = "a_very_large_string_with_special_chars_12345!@#"
# s2 = "a_very_large_string_with_special_chars_12345!@#"





# 6. Membership Operators
# Used to check if a value is in a sequence (list, tuple, set, dictionary, etc.).

# my_list: list = [1, 2, 3, 4, 5]
# string_text = "Operator system"
# print(1 not in  my_list)
# print("1" in string_text)








# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.
# # Valid variable names
# name = "Alice"
# _age = 25
# salary2024 = 50000
# my_variable = "Python"

# # Invalid variable names
# 2name = "Bob"          # ❌ Starts with a digit
# my-variable = "Error"  # ❌ Contains a hyphen
# class = "CS101"        # ❌ Uses a reserved keyword



myVA = 12
print(myVA)