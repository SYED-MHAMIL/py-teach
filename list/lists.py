# if __name__ == '__main__':
#     obj = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         obj.append({
#             "name" : name,
#             "score" : score
#         })
#     print(obj)
#     second_high = sorted(obj,key=lambda x:x["score"],reverse = True)
#     print(second_high[1]["score"])
#     second = []
#     for a in obj:
#         if second_high[1]["score"] == a["score"]:
#            second.append(a) 
    
#     second_high = sorted(second,key=lambda x:x["name"])
#     for man in second_high:
#         print(man["name"])




#  reomve ddelete first occurance and nothing return

listFruit = ["banana", "apple", "asngoor" ,"orange","banana"]
# f =listFruit.remove("banana")




# The pop() method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list.


# f = listFruit.pop(0)
# print(f)





# 1. Default Sorting (Ascending Order)
# Sorting a List


numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
# print(numbers)  # Output: [1, 1, 3, 4, 5, 9]



# reverse

# numbers.sort(reverse=True)
# print(numbers)  


# len abase sorting


# listFruit.sort(key=len)
# print(listFruit)  




#  ==============   Sorted by last charactor =================

# fruit =   ["banano", "apple", "asngoor" ,"orange","banana"]
# fruit.sort(key= lambda word:word[-1])
# print(fruit)

# import string
# def sorted(lis):
#     ordered_letter = []
#     alphabet = list(string.ascii_lowercase)
#     for a in alphabet:
#         for word in lis:
#             if word[-1] == a:
#                 ordered_letter.append(word)
#     return ordered_letter


# e =sorted(["banano", "apple", "asngoor" ,"orange","banana"])
# print(e)




# original = [[1, 2], [3, 4]]
# shallow = original.copy()  # or list(original) or original[:]

# shallow[0][0] = 99

# print("Original:", original)
# print("Shallow :", shallow)



# nested = [1, [2, [3, [4, 5]], 6],7]


# flatten = lambda lst:[x if isinstance(x,int) else flatten(x)  for x in lst]
# print(flatten(nested))

# [1, [2, [3, [4, 5]], 6], 7]


a=[i for i in range(5)] * 2
a[0]=80
print(a)




obj2 = {
    (1,2,3) :  "name"
}

print(obj2)

