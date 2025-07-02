# import math

# #  1. Count Prime Numbers in a File
# with open("number.txt","w") as file:
#     file.write("23,12,4,9,7,29,30,31")


# def isPrime(n):
#     if n<=1:
#         return False
#     if n == 2 :
#         return True
#     if n%2 == 0 :
#         return False
#     for i in range(3,int(math.sqrt(n))+1 ,2):
#         if n%i == 0 :
#             return False
#     return True
               

# with open("number.txt","r") as file:
#      data = file.read()
#      count = 0
#      for i in data.split(","):
#          if isPrime(int(i)):
#              count+=1
#      print(count)    
             




#  2. Group Words by First Letter
# File Content (words.txt):
# apple,banana,apricot,blueberry,cherry,avocado

# Task:
# Write a function group_words_by_letter() that:
# a_words.txt, b_words.txt, 
# Groups words by their first letter (case-insensitive).
# Writes each group into a separate file:etc.



# ======================  FIRST WAY  TO  SOLVE THIS QUESTION ===================

# def group_words_by_letter():
#     with open("words.txt",'r') as f:
#          data = f.read()
#          for g in data.split(","): #anggor
#              try:
#                 with open(f"{g[0]}_words.txt", "r") as f:
#                     data2 = f.read()
#                     if data2[0] == g[0]:
#                         # for i in data2.split(","): # apple ,anar
#                             if g not in data2.split(","):  
#                                 with open(f"{g[0]}_words.txt","a") as a:
#                                     a.write(","+g)
#              except FileNotFoundError:
#                     with open(f"{g[0]}_words.txt",'w') as f:
#                          f.write(g)
                  
# group_words_by_letter()
                 
    
# ====================== SECOND WAY  TO  SOLVE THIS QUESTION ===================


# def group_words_by_letter():
#     try:
#         with open("words.txt", 'r') as f:
#             words = f.read().strip().split(",")
#     except FileNotFoundError:
#         print("words.txt file nahi mili.")
#         return

#     for word in words:
#         word = word.strip()
#         if not word:
#             continue
#         filename = f"{word[0].lower()}_words.txt"
#         try:
#             with open(filename, 'r') as f:
#                 existing_words = f.read().strip().split(",")
#         except FileNotFoundError:
#             existing_words = []

#         if word not in existing_words:
#             with open(filename, 'a' if existing_words else 'w') as f:
#                 if existing_words:
#                     f.write("," + word)
#                 else:
#                     f.write(word)

# group_words_by_letter()



# practise  


# def group_words_by_letter():
#      try:
#           with open("words.txt",'r') as f:
#                words = f.read().strip().split(",")
#      except FileNotFoundError:
#           print("Doesn't exists as such file!")
#           return
#      for word in words:
#         word =word.strip()
#         if not word:
#              print(" WORRD NAHI HAIN ")
#              continue
#         filename = f"{word[0].lower()}_words.txt"
#         try:
#              with open(filename,"r") as f:
#                   existance_words = f.read().split(",")
#         except:
#               existance_words =[]
#         if word not in existance_words:
#              with open(filename, "a" if existance_words else "w") as file:
#                   if existance_words:
#                        file.write(f",{word}")
#                   else:
#                        file.write(word)              
# group_words_by_letter()
             
             
# def make_group_by_fletter():
#     try:
#         with open("words.txt",'r') as f:
#             words = f.read().strip().split(",")
#     except FileNotFoundError:
#          print("doennot exits as such file!")
    
#     for word in words:
#         word =word.strip()
#         if not word:
#            continue
#         filename = f"{word[0].lower()}_words.txt"
#         try:
#             with open(filename,'r') as f :
#                  existance_word = f.read().split()
#         except:
#             existance_word = []
#         if word not in existance_word:
#             with open(filename, "a" if existance_word else "w") as f:
#                if existance_word:
#                    f.write_through(","+word)
#                else:
#                    f.write(word)          
# make_group_by_fletter()





# Q# Folder data/ contains multiple .txt files with comma-separated integers.
# Task:
# Create a function sum_all_numbers() that:

# Loops over each .txt file in the folder.

# Sums all the integers across all files.

# Prints total sum.


import os

# def sum_all_numbers():

#     # Assign directory
#     directory = r"C:\Users\mohamil\Desktop\MHAMIL\PYTHON\PIAIC\py-teach\file-handle\data"
#     sum=0
#     # Iterate over files in directory
#     for name in os.listdir(directory):
#         if name.endswith(".txt"):
#             print(f"directory name is {name}")
#             with open(os.path.join(directory, name)) as f:
#                 integer = f.read().split(",")
#                 for i in integer:
#                     sum+=int(i)
#     print(f"your integer sun is {sum}")             
            
# sum_all_numbers()




# Q5 Task:
# Write a function validate_emails() that:
# Reads emails from the file.
# Validates format using regex.
# Writes valid emails to valid_emails.txt.
# Logs invalid ones to log.txt.


def checkEmail(e):
    if "@gmail.com" in e :
       return True
    else:
        return False

# def validate_emails():
#       directory = r"C:\Users\mohamil\Desktop\MHAMIL\PYTHON\PIAIC\py-teach\file-handle"
#       with open(os.path.join(directory,"emails.txt"),"r") as f:
#         emails =f.read().split(",")

#       isFoundvalid = False
#       isFoundnonvalid = False
      
#       for email  in emails:
#            isValidEmail = checkEmail(email)
#            try:
#                with open("valid_emails.txt" if isValidEmail else "logs.txt" ,"r") as f:
#                 existancedata = f.read().strip().split(",") 
#                 existancedata = [d.strip() for d in existancedata]
#            except:
#                existancedata =[]
               
#            if email.strip() not in existancedata:
#                 with open("valid_emails.txt" if isValidEmail else "logs.txt" ,"a") as f:
#                     if  isValidEmail:
#                         if isFoundvalid:
#                             f.write("," + email)
#                         else:
#                             f.write(email)
#                             isFoundvalid =True
#                     else:
#                         if isFoundnonvalid:
#                             f.write("," + email)
#                         else:
#                             f.write(email)
#                             isFoundnonvalid =True

# validate_emails()

# Open an image file in binary mode
with open("mhamil.txt", "rb") as image_file:
    image_data = image_file.read()
    print(image_data.decode('utf-8'))









