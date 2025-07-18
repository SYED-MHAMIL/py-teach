from collections import Counter
no_of_shoes= input()
size_all = Counter(list(map(int,input().split()))) 

values=list(size_all.values())
keys=list(size_all.keys())

N= int(input())
result=0
for i in range(N):
    customer_size = tuple(map(int,input().split()))
    if customer_size[0] in keys:
       index = keys.index(customer_size[0])
       if values[index] != 0:
          result+=customer_size[1]
          values[index]-=1


print(result)