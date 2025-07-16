A=[1,2]
B=[3,4]

r=[(a,b) for a in A for b in B]
r= sorted(r)
for i in r:
    print(i,end=' ')
