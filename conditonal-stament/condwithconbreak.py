def calculator():
    print("""
     you can basic operation here 
""")
    result = 0
    while True:
        operation_selected = ("/","*","+", "-","//","**","%")
        operation =  input("enter the basics operstion now! and 'q' off the calculator")
        if operation not in operation_selected :
            print("invalid oprator just alllow '*,**,/,//,%'")
            continue
        
        try:
            num1 =float(input("enter number 1"))
            num2 = float(input("enter the number 2 "))
        except ValueError:
            print("just numbe allowed")
            continue

        if operation == '+':
           result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero."
                print(result)
                continue
        elif operation == '%':
             result = num1 % num2
        elif operation == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                result = "Error: Division by zero."
                print(result)
                continue
        elif operation == '**':
             result = num1 ** num2 
    
        print (result)            

          
# calculator()


# def check_number(num):
#     match num:
#         case x if x > 0:
#             print("Positive number")
#         case x if x < 0:
#             print("Negative number")
#         case 0:
#             print("Zero")

# check_number(10)   # Output: Positive number
# check_number(-5)   # Output: Negative number
# check_number(0)    # Output: Zero




# def process_list(lst):
#     match lst:
#         case []:
#             print("Empty list")
#         case first,*second:
#             print(f"List with two elements: {first} and {second}")
#         case [first, *rest]:
#             print(f"First element: {first}, rest: {rest}")
#         case _:
#             print("Other case")

# process_list([])         # Output: Empty list
# process_list([1, 2])     # Output: List with two elements: 1 and 2
# process_list([1, 2, 3])  # Output: First element: 1, rest: [2, 3]



# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 6:
#         print("Number found!")
#         break
# else:
#     print("Number not found!")  # Runs because 6 is not in the list
     




# Sum numbers from 1 to 100
# total: int = 0
# for i in range(1, 101):
#     total += i
# print("Sum of numbers from 1 to 100:", total)



# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,5):
#     print("*" * i)



# Write a while loop that counts how many times a number n can be divided by 2 until it's less than 1.



n =45

# def howmany_count(n):
#     count =1
#     while True:
#          n = n/2
#          if n<1:
#              break
#          count+=1
         
#    *     
#   ***
#  *****
# *******


# for i in range(1,5):
#     for j in range(1):
#         print(i *"*")
    #     for i in range(1, 5):          # Outer loop controls rows
    # for j in range(i):         # Inner loop controls stars per row
    #     print("*", end="")
    # print()                    # Move to next line after inner loop



# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()
    
