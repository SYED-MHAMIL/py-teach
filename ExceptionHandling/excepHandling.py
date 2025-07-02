
# ## **Why Use Exception Handling?**

# *   **Prevents Program Crashes**: Ensures your program doesn’t terminate abruptly due to unexpected errors.

# *   **Graceful Error Recovery**: Allows you to handle errors gracefully and provide meaningful feedback to users.
# *   **Clean Code**: Separates error-handling logic from the main program flow, making code more readable and maintainable.
# *   **Resource Management**: Ensures resources (e.g., files, connections) are properly released, even if an error occurs.



# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(ZeroDivisionError)



# import random
# from typing import Tuple, Dict, List

# def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
#     """Generates a list of random number pairs."""
#     try:
#         if not isinstance(num_samples, int) or num_samples <= 0:
#             raise ValueError("Number of samples must be a positive integer.")
#         data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
#         return data
#     except ValueError as ve:
#         print(f"Error: {ve}")
#         return []  # Return empty list on error
#     except Exception as e: # Catch any other unexpected errors
#         print(f"An unexpected error occurred: {e}")
#         return []

# # print(generate_random_data(00000))



# def terminate_program():
#     """Terminates the program by raising an exception."""
#     raise SystemExit("Program is terminating.")

# terminate_program()




# try:
#     try:
#         raise ValueError("Inner")
#     except ValueError as e:
#         print("Caught inner:", e)
#         raise
# except ValueError as e:
#     print("Caught outer:", e)



#  becasue inner try raise the error and then reraised the error throgh raise keyword



# def test():
#     try:
#         return 3 
#     except:
#         return 6
#     else:
#         return 10
    
# print(test())

#  why is happening now because of try already return the valuse it function did not reach at else bloack


# try:
#     x = int("abc")
#     y = 5 / 0
# except ValueError:
#     print("Conversion failed")
# except ZeroDivisionError:
#     print("Divide by zero")

# because eror check that is in int("int")



# try:
#     raise KeyboardInterrupt("DASDASDasdasd")
# except BaseException:
#     print("Handled")
# finally:
#     print("Cleanup")




# try:
#     print("A")
#     raise KeyboardInterrupt("Stop")
# except Exception:  # because is not builtin eception error occured
#     print("B")
# finally:
#     print("C")



# ERROR HANDLING WITH FILE 
# import os

# current_dir = f"{os.getcwd()}/py-teach"

# try:
#     file = open(f"{current_dir}/mhamil.txt", "r")
#     data= file.read()
#     print(data)
# except FileNotFoundError as e:
#     print(f"your file mhamil.txt is{e}")
# except PermissionError:
#     print("Error :  Permission denied")
# else:
#     print("file has got successfully")
# finally:
#     try:
#         file.close()
#     except NameError:
#         print("ther are not file to access")
   
     



# def final_boss():
#     try:
#         raise ValueError("Outer Error")
#     except ValueError as e:
#         try:
#             raise KeyError("Inner Error")
#         except KeyError as ke:
#             raise RuntimeError("Final Blow") from e
#         finally:
#             print("Inner finally running")
#     finally:
#         print("Outer finally running")

# final_boss()




# in this exmaple following we saw what is cause chaning overwrite block skipped block 
#  and  more you can check (if needed)



def final_boss():
    try:
        x = 1/ 0
        raise ZeroDivisionError("Outer Error")
    except ValueError as e:
        try:
            raise KeyError("Inner Error")
        except KeyError as ke:
            raise RuntimeError("Final Blow") from e   # isthis case frrom e means cause  error is "e" ValuseError()
        finally:
            print("Inner finally running")
    finally:
        print("Outer finally running")

# try:
#     final_boss()
# except Exception as ex:
#     print("Caught:", ex)
#     print("Cause:", ex.__cause__)



# def callERror():
#     try:
#         final_boss()
#     finally:
#         print("error ayega")
# callERror()

    



# import random
# from typing import Tuple, Dict, List
# def random_number_GEnerate(num1:int)-> List[Tuple[int,int]] :
#     try:
#         if not isinstance(num1,int)  or num1<=0:
#             raise ValueError("just integer is allowed other wise you can't my website")
#         return [(random.randint(1,100),random.randint(1,100))   for _ in range(num1)]  
           
#     except ValueError as e:
#         print(f"Error: {e}")
#         return []
#     except Exception as e:
#         print(f"Error: unexpected error occured")
#         return []
    

# print(random_number_GEnerate(10))


class InvalidOperator(Exception):
      def __init__(self,message):
          super().__init__(message)
          
          
          
# import logging

   
# def calculator():
#     """WElCOME TO OVER BASICS ERROR HANDLING
#        CALCULATOR
#     """
#     while True:
#         try:
#             num =float(input("enter the num 1"))
#             opearater =input("give operaotr and q to exit")
#             if opearater == "q":
#                 break
#             if not  opearater in ("/","*","+","-"):
#                 raise InvalidOperator(f"just this operation (/,*,+,-) is allowed")
                    
#             num2 =float(input("enter the num 2"))
            
#             if opearater == "+":
#                 result = num +num2
#                 return result
#             elif opearater == "-":
#                 result = num -num2
#                 return result 
#             elif opearater == "*":
#                 result = num *num2
#                 return result 
#             else:    
#                 if num2 == 0:
#                     raise ZeroDivisionError("Division by zero")
#                 result = num /num2
#                 return result
        

#         except InvalidOperator as i:
#              logging.warning(f"ERROR {i}")
#         except ZeroDivisionError as e:
#              logging.warning(f"ERROR {e}")
#              continue                    
#         except ValueError as e:    
#             logging.warning(f"ERROR {e}")
#             continue
                       
#         except KeyboardInterrupt as e:
#             logging.critical(f"ERROR : your progrma is somthing going wrong{e}")
#             break
#         finally:
#             logging.info("thnak for use calcultor")        
         
                   
            
    
       
# print(calculator())









# ADVANCE

import logging
import ast
import operator
allowed_operation = {
     ast.Add : operator.add ,
     ast.Sub :operator.sub,
     ast.Mult : operator.mul,
     ast.Pow : operator.pow,
     ast.USub :operator.neg 
}


def eval_expression(node):
    try:
        if isinstance(node,ast.Expression):
           return  eval_expression(node.body) # "3343 * 3 * 8" 
        elif isinstance(node,ast.BinOp):
            left = eval_expression(node.left)  # 3 * 8  agin call fun and got 24 and 24 * 33343
            right = eval_expression(node.right)  # 33343
            op_type =type(node.op)
            print(f"type of  {op_type}")
            print(f'operaiton  {node.op}')

            if op_type in allowed_operation:
                return allowed_operation[op_type](left,right)
            else:
                raise TypeError(f"Unsupported operator you have given is {op_type}")
    
        elif isinstance(node,ast.Constant):
            return node.value
        else: 
            raise TypeError(f"Unsupported expression type {type(node)}")
    except TypeError as e:
        logging.error(f"ERROR: {e}")

    except Exception as e:
        logging.error(f"ERROR: {e}")
        








def calculator():
    """WElCOME TO OVER BASICS ERROR HANDLING
       CALCULATOR
    """
    while True:
        exp = input("")
        tree = ast.parse(exp,mode="eval")
        result = eval_expression(tree)
        if result == "q":
            break
        else:
            print(f"Reslut : {result}")

    

    
         
                   
            
    
       
print(calculator())






















#     ================        Want to Finish 100%?            ===============


# Let me know if you'd like short lessons or examples on:

# 📜 Logging errors to file (instead of just printing)

# 📉 Getting full traceback programmatically