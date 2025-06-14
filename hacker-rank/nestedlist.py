# You are given a list of students.
# Each student has:
# A name (string)
# A grade (float)

#  Your Task:
# Find the second lowest grade among all students.
# Identify the student(s) who have that second lowest grade.
# If there are multiple students with the second lowest grade:
# Sort their names alphabetically (A–Z).
# Print each name on a new line.



# if __name__ == '__main__':
#     obj = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         obj.append({
#             "name": name ,
#             "score": score
#         })
#     unique_scores = sorted({ entry["score"] for entry in obj },reverse = True)
#     print(unique_scores)   
#         # res=[sorted(records, key = lambda x:x["score"],reverse=True)]
   
    
    
# input = [[str(input("enter the name")),float(input("enter the score"))] for _ in range(int(input("enter which student's data have to store")))]

# sorter= sorted({a[1]  for a in input},reverse=True)
# second_highest =  sorter[1] 
# name =[   sorted( hasEqual[0] for hasEqual in input if hasEqual[1] == second_highest)]
# print(name)


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    high = sorted( {li[1]  for li in records },reverse= True)
    sec_high = high[1]
    sortedName = sorted( r[0] for r in records if r[1] == sec_high)
    for name in sortedName:
        print(name)







