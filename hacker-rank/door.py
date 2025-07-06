
N, M = map(int,input().split())
print(M)


# other way but we can correct

# for i in range(4):
#     print(((i)*".|.").rjust((M-1)//2,"-")+".|."+ ((i)*".|.").ljust((M-1)//2 ,"-") )
# for i in range(1):
#    print(((i +1)*"WEL").rjust((M-1)//2,"-")+"C"+ ((i+1)*"OME").ljust((M-1)//2 ,"-") )
# for i in range(4,0,-1): 
#     print(((i-1)*".|.").rjust((M-1)//2,"-")+".|."+ ((i-1)*".|.").ljust((M-1)//2 ,"-") )




# for i in range(4):
#     print(((i*2 +1)*".|.").center(27,"-"))
# for i in range(1):
#     print(("WELCOME").center(27,"-"))
# for i in range(4,0,-1):
#     print(((i*2-1)*".|.").center(27,"-"))





# for i in range(1,N,2):
#     print((".|."*i).center(M,"-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,0,-2):
#     print((".|."*i).center(M,"-"))




for i in range(1,N,2):
    print((i* ".|.").center(M,"-"))
for i in range(1):
    print(("WELCOME").center(M,"-"))
for i in range(N-2,0,-2):
    print(i*".|.").center(M,"-")

