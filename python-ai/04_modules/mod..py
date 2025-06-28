# def modify_value(x):
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(x)
# print("After function:", x)




# if you want change the global varible in function so we used gloab method

# x = 5
# def modify_value():
#     global x
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# print("Original:", x)
# modify_value()
# print("After function:", x)  # globally changed !



# You also want to change global and use same name varible so what can we do  
# x = 5
# def modify_value(x):
#     g=globals("a")
#     x = 10
#     print("Within function global variable:", g)
#     print("local same variable in :",x)
# # Immutable object (integer)
# print("Original:", x)
# modify_value(x)
# print("After function:", x)






# when you pass in list in  function what does behave list


# def modify_list(lst):
#     lst.append(5)
#     print("Within function: ", lst, " - ID:", id(lst))

# # Mutable object (list)
# lst = [1, 2, 3]
# print("Original:", lst, " - ID:", id(lst))
# modify_list(lst)
# print("After function:", lst, " - ID:", id(lst))



# Function arguments are the values or variables passed into a function when it is called.


# def greetings(name):
#    "This is docstring of greetings function"
#    print ("Hello {}".format(name))
#    return

# greetings("Ali")
# greetings("Omar")
# greetings("Usman")



# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age=50, name="Arif" )
# printinfo(50, "Arif" )



# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age=50, name="Arif" )
# printinfo( name="Arif" )

# def posFun(x, y, /, z):     # "/" represnts there before the "/" all argments must be 
#     # key-words argment
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(1, 2,3)

# # uncomment to see error
# posFun(x=1, y=2, z=3)




# Those arguments that must be specified by their `name` while calling the function is known as `Keyword-only arguments`. They are defined by placing an `asterisk ("*")` in the function's parameter list before any keyword-only parameters. This type of argument can only be passed to a function as a keyword argument, not a positional argument.



# def posFun(*, num1, num2, num3):   # in there case  "*" represents all parameter should key-word argument
#     print(num1 * num2 * num3)

# print("Evaluating keyword-only arguments: ")
# posFun(num1=6, num2=8, num3=5)
# posFun(num3=6, num1=8, num2=5)
# posFun(45,num3=6,num1=8)
# takes 0 positional arguments but 2 keyword argument were given



# TypeError: posFun() takes 0 positional arguments but 3 were given
#posFun(6, 8, 5)



