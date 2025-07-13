# Strings in Python
# In Python, a string is a sequence of characters enclosed in quotes (either single, double, or triple quotes). Strings are immutable, meaning they cannot be changed after they are created.

# Creating Strings
# There are several ways to create strings in Python:

# Single Quotes: my_string = 'Hello, World!'
# Double Quotes: my_string = "Hello, World!"
# Triple Quotes: my_string = '''Hello, World!''' (can span multiple lines)
# Raw Strings: my_string = r'Hello, World!' (treats backslashes as literal characters)


#for multi line string use triple quotes '''any string'''
my_string: str = '''Hello,
World!'''
print(my_string)



# Pool of String Literals in Python
# In Python, a pool of string literals is a mechanism used by the interpreter to manage memory allocation for string objects. When a string literal is encountered in the code, Python checks if an identical string already exists in memory. If it does, the new string is not created, and instead, a reference to the existing string is used.

# How it Works
# When Python encounters a string literal, it checks the following:

# Interning: Python checks if the string is already interned, meaning it has been created and stored in memory before. If it is, Python returns a reference to the existing string.
# String Literal Pool: If the string is not interned, Python checks the string literal pool, which is a cache(Pronunciation: kash) of recently created strings. If the string is found in the pool, Python returns a reference to the existing string.
# Create New String: If the string is not found in the pool or interned, Python creates a new string object and stores it in memory.
# Benefits
# The pool of string literals provides several benefits:

# Memory Efficiency: By reusing existing strings, Python reduces memory allocation and deallocation overhead.
# Performance: Looking up strings in the pool is faster than creating new strings.
# Internalization: The pool helps to internalize strings, making them more efficient to use in comparisons and other operations.
# Unicode characters
# Python also supports Unicode escape sequence characters, which are used to represent Unicode characters. These characters are denoted by \u followed by a four-digit hexadecimal code.

# Escape Sequence Characters in Python
# In Python, escape sequence characters are used to represent special characters that have a specific meaning in a string. These characters are denoted by a backslash (\) followed by a character.


# print(r"\u0041 = ", "\41")
# print(r"\u0042 = ", "\u0042")
# print(r"\u0043 = ", "\u0043")





# Performing Differrent Operations on String Object

# index() → Finds substring, raises error if not found.
# find() → Finds substring, returns -1 if not found (safer).
# Can specify start and end positions for more control.
# Use a loop if you need all occurrences of a substring.


# my_string = "Hello, World! Hello, Pakistan"
# # count the occurrences of a substring
# count = my_string.count('Hello')
# print("my_string.count('Hello') = ", count)  # prints 2

# # count the occurrences of a substring
# count = my_string.count('P')
# print("my_string.count('P')     = ", count)  # prints 1

# # count the occurrences of a substring
# count = my_string.count('o')
# print("my_string.count('o')     = ", count)  # prints 2

# # count the occurrences of a substring
# count = my_string.count('hello') # case sensitive
# print("my_string.count('hello') = ", count)  # prints 0






# String Formatting
# Python provides several ways to format strings:

# % Operator: my_string = 'Hello, %s!' % 'World'
# In Python, %s, %d, %c, %f are placeholders for values in a string. They are used with the % operator to insert values into a string.
# Note: The % operator is an older way of formatting strings in Python. The newer and more recommended way is to use the str.format() method or f-strings (introduced in Python 3.6). For example:
# str.format(): my_string = 'Hello, {}!'.format('World')
# f-Strings: my_string = f'Hello, {"World"}!'


my_string = 'Hello,%s!'% 'World'
print(my_string)




name: str = 'John'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000 # 70.536000

#uncomment to see type
#print(type((name, first_letter, age, my_weight)))
  
# using % operator
# my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (name, first_letter, age, my_weight)
# print(my_string)

# my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (name, first_letter, age, my_weight) # Dont forget period %.2f
# print(my_string)


# # Error: TypeError: %d format: a real number is required, not str
# my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (my_weight, age,45, first_letter)  



# a = "this is a very long string"
# b = "this is a very long string"
# print(a is b)  # False (not interned)
# print("id(a)", id(a))
# print("id(b)", id(b))






# prompt: print list of str functions using dir(), dont show function starting with"__"

# Get the list of string methods
sfilteredtring_methods: str = dir(str)

# Filter out methods starting with "__"
filtered_methods: str = [method for method in sfilteredtring_methods if not method.startswith("__")]

# Print the  list
# print(filtered_methods)


name: str = 'John'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000 # 70.536000

#uncomment to see type
#print(type((name, first_letter, age, my_weight)))

# using % operator    
# my_string: str ='My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.' % (name, first_letter, age, "DASdsa")
# print(my_string)

# my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (name, first_letter, age, my_weight) # Dont forget period %.2f
# print(my_string)





# using str.format()


# my_string: str = 'My name is {} and I am {} years old.'.format(age, name) #order matters
# print("line 1: ",my_string)

# my_string: str = 'My name is {1} and I am {0} years old.'.format(age, name) #use indexing
# print("line 2: ",my_string)


# my_str = 'my name is {} abd i am {} year'.format(34,'mhamil')
# my_str1 = 'my name is {1} abd i am {0} year'.format(34,'mhamil')
# print(my_str)
# print(my_str1)

# a = "OpenAI"
# print(a[::3])


# s = "ABCDE"
# print(s[-10:-2])


str1 = "Python"
print(str1[1:5:2])




