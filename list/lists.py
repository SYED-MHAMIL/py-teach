if __name__ == '__main__':
    obj = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        obj.append({
            "name" : name,
            "score" : score
        })
    print(obj)
    second_high = sorted(obj,key=lambda x:x["score"],reverse = True)
    print(second_high[1]["score"])
    second = []
    for a in obj:
        if second_high[1]["score"] == a["score"]:
           second.append(a) 
    
    second_high = sorted(second,key=lambda x:x["name"])
    for man in second_high:
        print(man["name"])
        