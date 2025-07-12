# Temporary Variables
# The single underscore is frequently employed as a temporary or throwaway variable. It signifies that the variable is used as a placeholder, and its value may not be utilized in the code.

# for _ in range(5):
#     print("Hello")



# Unused Variable
# In this example, a tuple is unpacked, and the underscore signifies that the second value is intentionally ignored in the program logic.




# he first element of t
# Function returning a pair of values
# def get_key_value_pair():
#     return "key", "value"

# _, value = get_key_value_pair()
# # Ignoring the first element of the returned pair using a single underscore

# # The first element is ignored, and only the second element is used
# print("Value:", value)





# Example 3: Single Underscore after a name 
# Python has its own default keywords which we can not use as the variable name. To avoid such conflict between python keyword and variable we use underscore after the name 




# class MyClass():
#     def __init__(self):
#         print("OWK")


# def my_definition(var1=1, class_=MyClass):
#     print(var1)
#     print(class_)


# my_definition()

# class MyClass():
#     def __init__(self):
#         print('owk')

# def fun(var1=1,class_=MyClass):
#     print(var1)
#     print(class_())

# fun()



# class Myclass():
#     def __init__(self):
#         self.__variable = 10

#     def func(self):
#         return self.__variable

# obj= Myclass()
# print(obj._Myclass__variable)






# =========================      Double Underscore in Python Examples :     ============
# Let us understand about double underscore in Python with the help of some examples:
# Name Mangling :
# When double underscores are used as a prefix in a class attribute name, it triggers a mechanism known as name mangling. This process alters the attribute's name to include the class name, preventing unintentional name clashes in subclasses.





#  ================== great example for double underscore   (NAME mangling) ==============
#==========================================
# class Parent():
#     def __init__(self):
#         self.__variable=10  


# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__variable=12

# ob =Child()
# print(ob._Child__variable)


# Now you have:

# c._Parent__value → 5

# c._Child__value → 10

# There’s no conflict, even though both used __value. That’s the point of name mangling — to protect variables in inheritance.

#  Summary (In Your Words):
# The leading double underscore tells the Python interpreter to rewrite the name to avoid conflict in a subclass. This feature is called name mangling. It adds _ClassName in front of the variable name.














# class MyClass:
#     def __init__(self):
#         self.__private_variable = 42
# # ​
# obj = MyClass()
# # Raises AttributeError; the name is now _MyClass__private_variable
# print(obj._MyClass__private_variable)
# # ​
# print(obj.__private_variable)