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