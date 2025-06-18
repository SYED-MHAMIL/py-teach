import math

#  1. Count Prime Numbers in a File
with open("number.txt","w") as file:
    file.write("23,12,4,9,7,29,30,31")


def isPrime(n):
    if n<=1:
        return False
    if n == 2 :
        return True
    if n%2 == 0 :
        return False
    for i in range(3,int(math.sqrt(n))+1 ,2):
        if n%i == 0 :
            return False
    return True
               

with open("number.txt","r") as file:
     data = file.read()
     count = 0
     for i in data.split(","):
         if isPrime(int(i)):
             count+=1
     print(count)    
             
         
