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




# ===========================    project start  ====================================
# ==========================                    ====================================


import os
import json
from datetime import datetime
import shutil
import re

script_directory_os = os.path.dirname(os.path.abspath(__file__))
# Using os module
folder = os.path.join(script_directory_os,'data')
CLEANED_CSV = os.path.join(folder,"all_employees_cleaned.csv")
JSON_FILE = os.path.join(folder,"employees.json")
BACKUP_DIR = os.path.join(folder,"backup")
 
def Back_up():
    if not os.path.exists(BACKUP_DIR):
       os.makedirs(BACKUP_DIR) 
    timestamp = datetime.now().strftime("%Y-%M-%d_%H-%M-%S")
    shutil.copy(CLEANED_CSV,f'{BACKUP_DIR}/all_employees_cleaned_{timestamp}.csv')
    shutil.copy(JSON_FILE,f'{BACKUP_DIR}/employees_{timestamp}.json')

def email_validate(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if  re.fullmatch(pattern,email):
        return True     
    else:
        return False

def validate_salary(salary):
    s = salary.replace('$',"")
    try:
         float(s)
         return True 
    except ValueError:
        return False
        
def log(msg):
    with open('logs.txt','a') as f:
         f.write(f'\n{msg}')   


 

def main():
    filelist  = os.listdir(folder)
    remove_dup = set()
    all_emloyess = []
    departments = {}
    
    filelist = [f for f in  filelist if f.endswith('txt')]    
    for file in filelist:
        
        department_name = file.replace(".txt","")
        departments[department_name]=[]
        print("file=>"+file)
        with open(os.path.join(folder,file),'r') as f:
            lines = f.readlines()
            print(lines)
            for line in lines:
                line= line.strip()
                emp_id,name,email,salary = line.split(",")
                if not email_validate(email):
                   log("invalid email")
                   continue
                if not validate_salary(salary):
                    log("invalid salary")
                    continue
                indenty = (emp_id,email)
                if indenty in remove_dup:
                    log('duplicate remove')
                    continue
                else:
                    remove_dup.add(indenty)
                departments[department_name].append({"id":emp_id, "name":name,"email":email,"salary":salary})
                cleaned_data =[department_name,emp_id,name,email,salary]
                all_emloyess.append(cleaned_data)
    import csv

    try:
        with open(os.path.join(folder,'all_employees_cleaned.csv'),'r') as f:
            f.readline()
            csvfile_exsits =[c.strip().split(',') for c in f.readlines() if not c == "\n"]
            print(f"csv exites is {csvfile_exsits} ")
            print(f"csv data is {all_emloyess} ")
    except FileNotFoundError:
        csvfile_exsits = []
    if not csvfile_exsits == all_emloyess :
        with open(os.path.join(folder,'all_employees_cleaned.csv'), 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['department','employess_id','name','email','salary']) 
                writer.writerows(all_emloyess)
                log("CSV WRITE SUCCESFULLLY")

    with open(os.path.join(folder,'employees.json'),'r') as f:
         exist_empoyess =json.load(f)
         exist_empoyess =exist_empoyess['departments'] 
         print(f"exists employess ---->>>{exist_empoyess}")
         print(f"all employess ---->>>{departments}")
         
    if not departments == exist_empoyess: 
        with open(os.path.join(folder,'employees.json'),'w') as f:
             json.dump({"departments":departments},f,indent=2)
             log("employees.json runs")

        
                                
    Back_up()       
main()

    
    
    





















# ===========================    project end ====================================











# def checkEmail(email):
#     for a in email:
#      if "@gmail.com" in a:
#         return True
    
#     return False




# import os     




# import os
# from pathlib import Path

# # Using os module
# current_working_directory_os = os.getcwd()
# script_directory_os = os.path.dirname(os.path.abspath(__file__))
# folder =  f"{script_directory_os}\\data"
# filelist  = os.listdir(folder)


# for file in filelist:
#     try:
#         with open(os.path.join(folder,file),"r") as data_one:
#             data =data_one.read().strip()
#             print(data)
#     except FileNotFoundError as e:
#          print(f"ERROR: {e}")

#     if checkEmail(data.split(",")) and data.split(",")[-1].isdigit():
#           try:
#               with open('all_employees_cleaned.csv','r') as extistfile:
#                     existanceData = extistfile.read().strip()
#           except FileNotFoundError:
#                existanceData=[]
                
#           if not data in existanceData:
#               with open("all_employees_cleaned.csv","a" if existanceData else "w") as f:
#                  if existanceData:
#                     f.write(f"\n{data}")
#                  else:
#                      f.write(data)                                      

# import json


# # csv to json

# def log(message):
#     with open("log.py",'a') as log:
#         log.write(message)

    




# try:
#     with open("all_employees_cleaned.csv","r") as csv:
#         csv_file = csv.read()
#         csv.seek(0)
#         csv_split = csv.read().splitlines()
#         print("csv file ::::::::::"+csv_file)   
# except FileNotFoundError as e:
#     print(f"Erorr{e}")

# try:
#     with open(f"{folder}\employees.json","r") as j:
#         json_file = j.read()
#         if json_file:
#             json_file = json.load(json_file,j)
#         print("csv file ::::::::::"+csv_file)   
# except FileNotFoundError as e:
#     json_file= []
#     print(f"Erorr{e}")

# for  e in  csv_split:
#   newMem=e.split(",")[0] 
#   if not newMem in json_file["department"]:
#     with open(f"{folder}\employees.json","w" if json_file else "w" ) as f:
#         if json_file:
#             data = json_file
#             memData=e.split(",")[1:]
#             data["department"][newMem]= memData
#             d =json.dumps(data)
#             f.write(d)
#         else: 
#               d = csv_split
#               obj ={
#                 "department" : {}
#               }
#               for a in d:
#                 b=a.split(",")
#                 obj["department"][b[0]]= b[1:]
#               js = json.dumps(obj)
#               print(f.write(js))


# with open("all_employees_cleaned.csv",'r') as f:
#     print(f.read().splitlines()[0].split(","))
#     d = f.read().splitlines()
#     obj ={
#         "department" : {}
#     }
#     for a in d:
#         b=a.split(",")
#         obj["department"][b[0]]= b[1:]


























# import os
# import json
# from pathlib import Path

# def checkEmail(email):
#     return "@gmail.com" in email

# # Setup directory and file paths
# script_directory = os.path.dirname(os.path.abspath(__file__))
# data_folder = os.path.join(script_directory, "data")
# cleaned_csv_path = os.path.join(script_directory, "all_employees_cleaned.csv")
# json_path = os.path.join(data_folder, "employees.json")

# # Read and clean each file from /data
# filelist = os.listdir(data_folder)
# for file in filelist:
#     file_path = os.path.join(data_folder, file)

#     try:
#         with open(file_path, "r") as f:
#             data = f.read().strip()
#             print(f"READ: {data}")
#     except FileNotFoundError as e:
#         print(f"ERROR: {e}")
#         continue

#     parts = data.split(",")

#     # Validate: must have at least 4 fields, valid email, and numeric salary
#     if len(parts) == 5 and checkEmail(parts[3]) and parts[4].replace("$", "").isdigit():
#         try:
#             with open(cleaned_csv_path, "r") as f:
#                 existing_data = f.read().strip().splitlines()
#         except FileNotFoundError:
#             existing_data = []

#         if data not in existing_data:
#             with open(cleaned_csv_path, "a" if existing_data else "w") as f:
#                 f.write("\n" + data if existing_data else data)
#                 print(f"APPENDED to cleaned CSV: {data}")

# # Convert CSV to JSON format
# try:
#     with open(cleaned_csv_path, "r") as csvfile:
#         lines= csvfile.read().splitlines()
#         print(f"CSV READ: {lines}")
# except FileNotFoundError:
#     lines = []
#     print("No CSV file found.")

# # Initialize or load existing JSON
# try:
#     with open(json_path, "r") as jf:
#         content = jf.read().strip()
#         if content:
#             json_data = json.loads(content)
#         else:
#             json_data = {"department": {}}
# except FileNotFoundError:
#     json_data = {"department": {}}


# # Update JSON with cleaned CSV data
# for line in lines:
#     parts = line.split(",")
#     if len(parts) == 5:
#         department, emp_id, name, email, salary = parts
#         entry = [emp_id, name, email, salary]

#         if department not in json_data["department"]:
#             json_data["department"][department] = []

#         # Avoid duplicate entries in JSON
          
#         if entry not in json_data["department"][department]:
#             json_data["department"][department].append(entry)
#             print(f"ADDED to JSON: {entry}")

# # Save the updated JSON
# with open(json_path, "w") as jf:
#     d=json.dumps(json_data)
#     jf.write(d+"10")
#     print(f"JSON FILE WRITTEN at {json_path}")
