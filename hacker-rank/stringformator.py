# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above for each  from i  to number. Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.




def string_formater(number):
    widht =  len(bin(number)[2:])
    for i in range(1,number):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(number)[2:]
        print(deci.rjust(widht), octa.rjust(widht), hexa.rjust(widht), bina.rjust(widht))    



if __name__ == '__main__':
    n= int(input())
    string_formater(n)









# def print_formatted(number):
#     width= len(bin(number)[2:])
    
#     for i in range(1,number+1):
#         dec1= str(i)
#         octe=oct(i)[2:]
#         hexa = hex(i)[2:].upper()
#         bina = bin(i)[2:]  
#         print(dec1.rjust(width), octe.rjust(width), hexa.rjust(width), bina.rjust(width))
        

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)