# num_int: int = 42

# print(type(num_int)," num_int = ",num_int,)  





# num_float: float = int(3.14)
# #num_float: float = .14

# print(type(num_float), " num_float = ", num_float)  # <class 'float'>




# list 

# my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
# my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

# print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
# print(type(my_list), " my_list   =  " + str(my_list))
# print(type(3+2j)) 



#         ====================    Tuple  ================

# The data should not change (it's immutable).

# Example: coordinates, dates, fixed configurations
# coordinates = (45.0, 90.0)
# You want to protect the data from being modified.

# Tuples prevent accidental changes in your program.

# You want to use the d ata as a key in a dictionary or in a set.

# Only immutable types like tuples can be used as keys.

# You care about performance.

# Tuples use less memory and are slightly faster than lists.

# location = {
#     (33.6844, 73.0479): "Islamabad"
# }

# print((location[(33.6844, 73.0479)]))

    




# my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
# print(my_tuple[0])
 



#         ====================    RANGE  ================



# num_range: range = range(1, 10, 2) # range(start, stop, step)
# print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>



## Accessing Real and Imaginary Part
# Python provides attributes .real and .imag to extract the real and imaginary parts of a complex number.

# z = 3j + 4j +1 + 23 +45 
# z = 3 + 4j

# print("Real Part:", z.real)   # Output: 3.0
# print("Imaginary Part:", z.imag)  # Output: 4.0




# 3. Sequence Types
# These store multiple items in an ordered way.

# ##a. String (str)
# A sequence of characters enclosed in quotes.