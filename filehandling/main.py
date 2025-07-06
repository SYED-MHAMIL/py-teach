# # Read multiple text files from a given directory (data/) where each file represents a department's employee records.
# # Each file is named like: hr.txt, engineering.txt, marketing.txt
# # Each line of a file has format: employee_id,name,email,salary
# # Clean and validate the data:
# # Remove duplicates.
# # Ensure email format is valid.
# # Filter out entries with salary not being a valid number.
# # Store cleaned data into a single file called all_employees_cleaned.csv.


# # Convert the final CSV into a JSON file named employees.json with the following structure:


# # {
# #   "departments": {
# #     "hr": [...],
# #     "engineering": [...],
# #     "marketing": [...]
# #   }
# # }

# # Add logging of the process to a log.txt file, including:

# # Number of lines read.
# # Number of valid entries.
# # Errors encountered (if any).

# # Implement exception handling for:
# # File not found
# # Incorrect data format


# # Bonus Task:
# # Create a backup of the cleaned CSV and JSON files in a folder named backup/ with a timestamped filename.





def checkEmail(email):
    for a in email:
     if "@gmail.com" in a:
        return True
    
    return False




import os     




import os
from pathlib import Path

# Using os module
current_working_directory_os = os.getcwd()
script_directory_os = os.path.dirname(os.path.abspath(__file__))
folder =  f"{script_directory_os}\\data"
filelist  = os.listdir(folder)


for file in filelist:
    try:
        with open(os.path.join(folder,file),"r") as data_one:
            data =data_one.read().strip()
            print(data)
    except FileNotFoundError as e:
         print(f"ERROR: {e}")

    if checkEmail(data.split(",")) and data.split(",")[-1].isdigit():
          try:
              with open('all_employees_cleaned.csv','r') as extistfile:
                    existanceData = extistfile.read().strip()
          except FileNotFoundError:
               existanceData=[]
                
          if not data in existanceData:
              with open("all_employees_cleaned.csv","a" if existanceData else "w") as f:
                 if existanceData:
                    f.write(f"\n{data}")
                 else:
                     f.write(data)                                      

import json


# csv to json

def log(message):
    with open("log.py",'a') as log:
        log.write(message)

    




try:
    with open("all_employees_cleaned.csv","r") as csv:
        csv_file = csv.read()
        csv.seek(0)
        csv_split = csv.read().splitlines()
        print("csv file ::::::::::"+csv_file)   
except FileNotFoundError as e:
    print(f"Erorr{e}")

try:
    with open(f"{folder}\employees.json","r") as j:
        json_file = json.loads(j.read())
        print("csv file ::::::::::"+csv_file)   
except FileNotFoundError as e:
    json_file= []
    print(f"Erorr{e}")

for  e in  csv_split:
  newMem=e.split(",")[0] 
  if not newMem in json_file["department"]:
    with open(f"{folder}\employees.json","w" if json_file else "w" ) as f:
        if json_file:
            data = json_file
            memData=e.split(",")[1:]
            data["department"][newMem]= memData
            d =json.dumps(data)
            f.write(d)
        else: 
              d = csv_split
              obj ={
                "department" : {}
              }
              for a in d:
                b=a.split(",")
                obj["department"][b[0]]= b[1:]
              js = json.dumps(obj)
              print(f.write(js))


# with open("all_employees_cleaned.csv",'r') as f:
#     print(f.read().splitlines()[0].split(","))
#     d = f.read().splitlines()
#     obj ={
#         "department" : {}
#     }
#     for a in d:
#         b=a.split(",")
#         obj["department"][b[0]]= b[1:]