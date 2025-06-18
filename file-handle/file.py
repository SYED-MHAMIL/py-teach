#    ***************** KEY POINT  ************************
# 1) when you use python write and append mode so python by deafult create the file 
# 2) when you use a+ mode cursor is move at he end then check 
# 3) when you use w mode cursor shit at the start and overwrite 
# 4)'w+' delete you can say s terncate first then execute 



# file = open("test.txt", "w")
# file.write("hello")
# file.close()


# new syntax of file handlng if we you want to does not clost file you can use it
  
# with open('test.txt','r') as file :
#     #  print(file.read())
#      print(file.readline())



#  center me add krna




# you have to do r+ and w+ 


# with open('test.txt', "w+") as f:
#     f.w



#    ***************** KEY POINT  ************************
# when you use python write and append mode so python by deafult create the file 




# ================= practise =======================

# &&&&&&&&&&&&&&&&&   RED  &&&&&&&&&&&&


# f = open("test.txt", "r")
# print(f.read())
# line = f.readline()
# print(line)
# f.close()

# f1 = open("test.txt", "r")
# # print(f.read())
# line = f1.readline()
# print(line)
# line = f1.readline()
# print(line)
# f1.close()


# &&&&&&&&&&&&&&&&&  write  MODE means overrite ok  &&&&&&&&&&&&

# f = open("practical.txt", "w")
# f.write(" the quiz of python has been conducted 19 may so we have to prepaaraiton")
# print(f.read())  # throw error beacuse  strict mode just you can write
# f.close()


# &&&&&&&&&&&&&&&&&  append  MODE means overrite ok  &&&&&&&&&&&&

# f = open("mhamil.txt",'a')
# f.write("\n who is mohamil ? \n mohamil is a passionate  ai engineer")







# &&&&&&&&&&&&&&&&&  read + write   &&&&&&&&&&&&
#  in this case write will not overwrite bec in r+ mode

# f = open("practical.txt","r+")
# f.write("faizi")
# print(f.read())
# f.close()


#   *************  w+ means write but with overwrite  +read =====================

# f = open("practical.txt","w+")
# f.write("offcourse")
# print(f.read())



# ===================  a+ means appendwrite +read =====================

# f = open("practical.txt","a+")
# print(f.read())
# f.write(" i am a millionar")






#  ============================    WITH KEYWORD  =======================

# what does with keyword work ?
# ans)  with keyword convience you that to use io setem without file closing b/c that are orginiziig in backend
# in short you dont need to maulally close the file as such  file.close()  



# with open("filname","mode") as file:
        # file.mode




#  ==============    DELETE THE FILEName  =====================
# import os 
# os.remove('test.txt')








#  ==============    DELETE THE FILEName  =====================

# with open("practise.txt",'w') as f:
#     f.write("Hi everyone \nwe are learning file I/O \nusing java \ni like programing in java")

# with open("practise.txt", 'r') as f:
#      data = f.read()
#      d1= data.replace("java","python")
     

# with open("practise.txt", 'w') as f:
#      f.write(d1)
     
     
# with open("practise.txt", 'r') as f:
#       d= f.read()
#       i =  d.find("learning")
#       if i == -1:
#            print("not exits as such name")
#       else:
#           print(f"yes and string indx no is {i}")
      

# with open("practise.txt", 'r') as f:
#     data = True
#     line =1
#     while data:
#         l1 =f.readline()
#         if (l1.find("learning") != -1):
#                 print("found")
#                 print(f' the line no is {line}')
#                 data = False
#         else:
#              line+= 1                

def findevenno():
    with open("practise.txt",'r') as f:
        d= f.read()
        count =0
        for a in d.split(","):
            if int(a)%2 == 0:
                count +=1
        print(count)
            
                
            
findevenno()
    
   

