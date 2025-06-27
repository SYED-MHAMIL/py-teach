# def swap_case(s):
#     # zain ASD
#     return ''.join([c.lower() if c.isupper() else c.upper() for c in s])

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)





def swap_case(s):
    st= s.split(" ")
    strlist = [c.lower() if c.isupper() else c.upper() for s in st for c in s]
    newStr =" ".join(strlist)
    return newStr

    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



