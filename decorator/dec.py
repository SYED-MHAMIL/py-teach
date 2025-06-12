#what is decorador by the way , a decorader is a unique to make callback and wrapper means that edit the functin


# ===================== Syntax of Decorator Parameters


# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         # Add functionality before the original function call
#         result = func(*args, **kwargs)
#         # Add functionality after the original function call
#         return result
#     return wrapper

# @decorator_name
# def function_to_decorate():
#     # Original function code
#     pass





# def greet(fn):
#     def fmx():
#         print("syed dus sadat hain")
#         fn()
#     return fmx



# @greet
# def name():
#     print("mhmaail")


# name()





# Q2 ???????????????????????


# def login(fx):
#     def mfx(*args,**kwargs):
#         print("you have succesfull login and contiue to your journry with mohamilAI")
#         fx(*args,**kwargs)
#     return mfx


# @login
# def data(arg):
#     print(arg)

# data(1)
    


# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # for _ in range(num_times):
#                 func(*args, **kwargs)   
#                 print(args)
#         return wrapper
#     return decorator
  
# # @repea(3)
# # def greet(name):
# #     print(f"Hello, {name}!")

# # greet("Alice")
# @repeat(2)
# def add(a, b,**kwargs):
#     print(a + b,kwargs)


# add(2, 3,red = "red",yellow = "yellow")













#   ==========     Q3) two wapper expample    == ====== ==== ========= ===#

# def star(fx):
#     def wrapper(*args,**kwargs):
#         print("*" * 15)
#         fx(*args,**kwargs)
#         print("*" *15 )
#     return wrapper 

# def percent(fn):
#     def wrapper(*args,**kwargs):
#         print("%" * 15)
#         fn(*args,**kwargs)
#         print("%" * 15)
#     return wrapper
  
   
 

# @percent
# @star
# def printer(msg):
#     print(msg)

# printer("Hello")


################ Q4)    ##############
import time 
 
# def timer(fn):
#     def wrapper():
#         start = time.time()
#         # Simulate slow code
#         time.sleep(2)
#         end = time.time()
#         elapsed = end - start
#         print(f"{fn.__name__} took {elapsed:.4f}")
        
#         fn()
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(2)
#     print("Done")
# slow_function()





#   Q# Task: Create a decorator @repeat(n) that repeats a function n times.


# def repeat(n):
#     def decortor(fn):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                  fn(*args,**kwargs)
            
#         return wrapper
#     return decortor

# @repeat(3)
# def greet(name):
#     print(f"hi {name}")

# greet("ali")




# Task: Create a decorator @only_even_args that raises an error if any argument passed to the function is odd.


# def only_even_args(fn):
#     def wrapper(*args,**Kwargs):
#         even = fn(*args,**Kwargs)
#         if even%2 ==0:
#             print("Work")
#         else:
#             print("ERror")
#     return wrapper




# @only_even_args
# def add(a, b):
#     return a + b



# add(3,4)
# add(2,4)



