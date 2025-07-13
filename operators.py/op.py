# class Person: 
#     def __init__(self, name):
#         self._name = name  # internal use only

# p = Person("Alice")
# print(p._name)  # This works, but it's discouraged




# -   The **walrus operator** `:=` was introduced in Python 3.8.
    
# -   It allows **assignment and evaluation** in a single expression.
    
# -   Great for use in **loops** or **conditional statements** to reduce redundancy.
    
# -   Example: `if (n := len(data)) > 10:` assigns and checks in one go.
    
# -   It improves readability and efficiency when used wisely!

# if (u:=input("enter num : ").isdigit()):
#     print(f"hello {u}")
# else:
#     print("sorty")









# Chained operator  


# x: int = 15
# if 10 < x< 20:
#     print("x is between 10 and 20")
# else:
#     print("not done")






# *****************************

# BYTES immmutable list

# *****************************



# byte = b'data'
# print(byte)

b =bytearray(b'heloo')
b[0]=56
print(b)


