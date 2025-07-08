# size 3

# ----c----   
# --c-b-c--  bc
# c-b-a-b-c  abc
# --c-b-c--
# ----c----








#  CHANGE A LITTLE BIT

# def print_rangoli(size):
#     alphabet = "abcdefghijklmnopqrstwvxyz"
#     alphabet=alphabet[:size]    
#     indies = list(range(size))  # let say : 0,1,2
#     indies =indies[:-1]+ indies[::-1]  # 0,1,2,1,0
    
#     for i  in indies:
#         strat_indies = i+1
#         right = alphabet[-strat_indies:]
#         left = right[1:]
#         left = left[::-1]
        

#         row = left + right
#         row= "-".join(row)
#         print(row.center(size*4 -3,'-'))   

# print_rangoli(3)
