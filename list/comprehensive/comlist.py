# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.



# with out comprehensive list

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)





##################  After  COMPREHENSIVE  #################

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

# print(newlist)  



# ====================    Exmaple

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [n for upper in mat  for n in upper ]

# print(res)





#Q2 #make thid from list comprehensive [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


# Nested list comprehension
matrix = [[n for n in range(5)] for i in range(5)]
# print(matrix)




# Example 2: Filtering a Nested List Using List Comprehension
# Here, we will see how we can filter a list with and without using list comprehension.

# Without Using List Comprehension

# In this example, a nested loop traverses a 2D matrix, extracting odd numbers from Python list within list and appending them to the list odd_numbers. The resulting list contains all odd elements from the matrix.


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_numbers = []
for mat in matrix:
    for m in mat:
        if m%2 != 0 :
           odd_numbers.append(m)
# print(odd_numbers)

#    ===========   FROM LIST COMPREHENSIVE

odd =[m for mat in matrix for m in mat if m%2 != 0]
# print(odd)





#  Example #: 
#    you have this following promlem  yo have to above 50 mark student's list with list comprehensive



data = [
    {"name": "Ali", "marks": {"Math": 60, "English": 55}},
    {"name": "Sara","marks": {"Math": 70, "English": 45}},
    {"name": "Zara", "marks": {"Math": 90, "English": 95}},
]



# import json

# unique_data = list({json.dumps(d, sort_keys=True) for extract in data})
# unique_data = [json.loads(d) for d in unique_data]




# result  = [d["name"] for d in data if all( k >=50 for k in d["marks"].values() )] 
# result = [d["name"] for d in data if all(k >=50 for k in d["marks"].values())]
# # print(result)



# {"name": "Ali", "marks": {"Math": 60, "English": 55}},
# for  d in data: 
#      if all(k>50 for k in d["marks"].values()):
#           print(d["name"])
     



     # Without if condition
# squared: list = [x**2 for x in [1, 2, 3, 4, 5] if x>3] #  if x > 3 place this if condition and see
# print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]


# print(squared)




