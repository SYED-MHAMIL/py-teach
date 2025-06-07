obj = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    obj.append({
        "name" : name ,
        "score" : score
    })
for key in obj:
    print(obj[key])