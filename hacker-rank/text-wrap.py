import textwrap

def wrap(string, max_width):
     
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)













# ==================   MAKE  TEXT WRAPPER OWN=================



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
# import textwrap


# def wrap(string, max_width):
#     arr = []
#     for i in  range(len(string)+1//max_width):
#         # 1st way :arr.append(string[i*max_width:((i+1)*max_width)])
        
#         # second way
#         chunks = [string[i:i+max_width] for i in range(0,len(string),max_width)]
        
#     return chunks
    

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     for i in result:
#         print(i)

# print(len("dsadasde")//4+1)
# print(6//4+1)
# stringg = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# chunks =[stringg[i:i+4] for i in range(0,len(stringg),4)]
# print(chunks)



