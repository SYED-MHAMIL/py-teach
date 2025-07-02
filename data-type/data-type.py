num_int: int = 42




# print(type(num_int)," num_int = ",num_int,)  

# print("hello world")



# num_float: float = int(3.14)
#num_float: float = .14

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
 



        # ====================    RANGE  ================



# num_range: range = range(1, 10, 2) # range(start, stop, step)
# print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>



# Accessing Real and Imaginary Part
# Python provides attributes .real and .imag to extract the real and imaginary parts of a complex number.

# z = 3j + 4j +1 + 23 +45 
# z = 3 + 4j

# print("Real Part:", z.real)   # Output: 3.0
# print("Imaginary Part:", z.imag)  # Output: 4.0




# 3. Sequence Types
# These store multiple items in an ordered way.

# ##a. String (str)
# A sequence of characters enclosed in quotes.





# byte_array: bytearray = bytearray(b'hello') #99c, 66=B ....decimal number system
# print(type(byte_array), " byte_array = ", byte_array)  # <class 'bytearray'>
# print(byte_array)
# print(chr(byte_array[3]))
# sec_byte : bytearray= bytearray()
# print("Empty bytearray(): ",sec_byte)


# # 4. 🧪 Convert Text to Bytes and Back
# text = "string"
# b = bytearray(b'string')  # Encode
# print(b )  # bytearray(b'hello')

# # Convert back
# print(b.decode())  # 'hello'





# import pickle
# import json 
# pickle ={
#      "dumps": lambda x: json.dumps(x) ,
#      "loads" :lambda x: json.loads(x)
# }
# obj = {"name": "Ali", "age": 25}

# # Convert (serialize) object to bytes
# b = bytearray(pickle["dumps"](obj))
# print(b)  # Now it's stored in byte format

# Convert back (deserialize)
# original_obj = pickle.loads(b)
# print(b)  # Output: {'name': 'Ali', 'age': 25}




# byte_data: bytes = b"Hello"
# print(type(byte_data), " byte_data = ", byte_data[0])  # <class 'bytes'>

# decoded_text = byte_data.decode('utf-8')
# print(decoded_text)
# # text = "Hello"
# # b = bytes(text, 'utf-8')  # Convert string to bytes
# # print(b[1])  # Output: b'Hello'





# d =bytearray(b"hello")
# d[0]=34

# print(d)

# Open an image file in binary mode
# with open("M.jpeg", "rb") as image_file:
#         image_data = image_file.read()

#         print(image_data)


# with open("Apollo11.jpg", "rb") as source_file:
#     data = source_file.read()

# # Write the binary data to a new image file
# with open("copy.jpg", "wb") as target_file:
#     target_file.write(data)

# print("Image copied successfully!")







# # Creating a bytearray object
# ba: bytearray = bytearray(b"hello")
# print("Before: ba = ", ba)

# # Modifying the bytearray
# ba[0] = 72  # ASCII value of 'H'

# print("After: ba = ",ba)  # Output: bytearray(b'Hello')





#  +++++++++++++++++         MEMORYVIEW            ++++++++++++++++

# mem_view: memoryview = (b"Operation Badar")
# print(type(mem_view), " mem_view = ", mem_view)  # 
# print(bytes(mem_view[0:4]))
# print( mem_view[6:11] ) #cast it to byte otherwise it will show memory address





# data = b"hello"
# slice1 = data[0:3]
# slice2 = data[0:3]
# print(id(slice1))  # Different ID (new object)
# print(id(slice2))
# print(slice1 is slice2)  # False




# None Data Type in Python
# In Python, None is a special data type that represents the absence of a value or a null object reference. It is a singleton object, meaning that there is only one instance of None in the entire Python environment.


# x: str = None
# y: str = None
# z: str = x

# #display the data type of x:
# print(type(x))                           # NONE
# print("value of x = " + str(x) )         # string 
# print("x == y = ", x == y)
# print("id(x) = ", id(x))
# print("id(y) = ", id(y))
# print("id(z) = ", id(z))
# print("x is y = ", x is y)
# print("x is z = ", x is z)
# print("id(x) is id(z) = ", id(x) is id(z)) # False :( why? you will get the answer in topic 'Integer Literals in Python'
# print("id(x) == id(z) = ", id(x) == id(z)) # True



x = 500   # object diff
z = 500   # object diff
y =x    # object same as  x

#   -5 to 286 range as in integer if  outsite this range is always should reutrn false  
# print(x is z)    # true
# print(x is y)  #True  

# ❌ Mistake in Code:
# You're doing:


# id(x) is id(y)
# But id(x) returns an integer (memory address), so you're comparing two integers with is, which is not recommended.

# 👉 Use == instead of is for comparing numbers/IDs:



# print(id(x) == id(z))
# print(500 is 500)


# a = 12
# b = 12
# c =  b

# print(id(b) is id(a))
# # print(type (id(x)))
# print(id(100) is id(100))


# x = 1000
# y = 1000
# print(x is y)




# =====================   MEMORY  VIEW  vs BYTES,BYTESARRAY    ==================




# BYTE ARRAY

data = bytearray(b'HelloStart')
slice_copy = data[0:2]  # creates a NEW copy: b'ell'
slice_copy[1] =88      # changes the copy, not the original
print(slice_copy)
print(data)       # bytearray(b'hello') ← original not changed




# MEMORY VIEW
# data = bytearray(b'Hellokarachi')
# mem = memoryview(data)
# view = mem[4:8]
# view[0] = 88
# print(bytes(view))   # its just view not a copy
# print(bytes(mem))