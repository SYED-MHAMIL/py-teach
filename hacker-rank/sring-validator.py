# Task

# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


# if __name__ == '__main__':
#     s = str(input())
#     if s.isalnum():
#         print("True")
#     else:
#          print("False")
    
#     for a in s:
#         if a.isalpha():
#             print("True")
#             break
#         if a.isalpha():
#             print("False")
#             break
#     for a in s:
#         if a.isdigit():
#             print("True")
#             break
#         if a.isdigit():
#             print("False")
#             break
#     for a in s:
#         if a.islower():
#             print("True")
#             break
#         if a.islower():
#             print("False")
#             break
#     for a in s:
#         if a.isupper():
#             print("True")
#             break
#         if a.isupper():
#             print("False")
#             break
        



# =======================    ALSOE USE ANY LIST COMREHENSIVE   ========================



# print(any( a.upper() for a in str(input())))
# any(itrator  : if in value of itrator is true it reutrns True)

# if __name__ == '__main__':
#     s = str(input())
#     if s.isalnum():
#         print("True")
#     else:
#          print("False")
#     has_true = False
#     for a in s:
#         if a.isalpha():
#             has_true =True
#             break
#     print("True" if has_true else "False")
        
#     for a in s:
#         if a.isdigit():
#             has_true =True
#             break
#     print("True" if has_true else "False")
#     for a in s:
#         if a.islower():
#             has_true =True
#             break
#     print("True" if has_true else "False")

#     for a in s:
#         if a.isupper():
#             has_true =True
#             break
#     print("True" if has_true else "False")
        

# thickness = int(input()) # 5
# c="H"

# for a in range(thickness):
#     print((a*c).rjust(thickness-1) + c + (a*c).ljust(thickness-1))
# for a in range(thickness +1):
#     print((thickness*c).center(thickness*2) + (thickness*c).center(thickness * 6))
# for a in range(thickness - 2):
#     print(((thickness*6 -2)*c).rjust(thickness*6 )    )
# for a in range(thickness +1):
#     print((thickness*c).center(thickness*2) + (thickness*c).center(thickness * 6))    
# for a in range(thickness,0,-1):
#     print(((a-1)*c).rjust(thickness) +c+ ((a-1)*c).ljust(thickness))
        



# thickness = int(input()) # 5
# c="H"

# for a in range(thickness):
#     print((a*c).rjust(thickness-1) + c + (a*c).ljust(thickness-1))
# for a in range(thickness +1):
#     print((thickness*c).center(thickness*2) + (thickness*c).center(thickness * 6))
# for a in range(thickness - 2):
#     # print((((thickness*6) - (thickness-3))*c).rjust(thickness*6 ))
#     print(((thickness *5) *c).center(thickness*6))
# for a in range(thickness +1):
#     print((thickness*c).center(thickness*2) + (thickness*c).center(thickness * 6))    
# for a in range(thickness,0,-1):
#     print(((a-1)*c).rjust(thickness *5 -1) +c+ ((a-1)*c).ljust(thickness))    
    
    
# print(len("HHHHHHHHHHHHHHHHHHHHHHHHHH"))


