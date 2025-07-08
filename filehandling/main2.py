# import os
# import csv
# import json
# import shutil
# from datetime import datetime

# script_directory_os = os.path.dirname(os.path.abspath(__file__))
# BACKUP_DIR = "backup"
# CLEANED_CSV = "all_employees_cleaned.csv"
# JSON_FILE = "employees.json"
# LOG_FILE = "log.txt"
# DATA_DIR = os.path.join(script_directory_os,'data')


# # Helper functions
# def is_valid_email(email):
#     return "@" in email and "." in email.split("@")[-1]

# def is_valid_salary(salary):
#     try:
#         float(salary.replace("$", ""))
#         return True
#     except ValueError:
#         return False

# def write_log(message):
#     with open(LOG_FILE, "a") as log:
#         log.write(message + "\n")

# def create_backup():
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     if not os.path.exists(BACKUP_DIR):
#         os.makedirs(BACKUP_DIR)
#     shutil.copy(CLEANED_CSV, f"{BACKUP_DIR}/all_employees_cleaned_{timestamp}.csv")
#     shutil.copy(ONJS_FILE, f"{BACKUP_DIR}/employees_{timestamp}.json")

# def main():
#     all_employees = []
#     departments = {}
#     seen_entries = set()

#     write_log("Starting processing...")
#     print("Starting processing...")

#     try:
#         files = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]
#         print(f"Found files: {files}")

#         for filename in files:
#             department = filename.replace(".txt", "")
#             departments[department] = []
#             filepath = os.path.join(DATA_DIR, filename)
#             print(f"Processing file: {filepath}")

#             try:
#                 with open(filepath, "r") as file:
#                     lines = file.readlines()
#                     write_log(f"{filename}: {len(lines)} lines read")
#                     print(f"{filename}: {lines,len(lines)} lines read")

#                     for line in lines:
#                         parts = line.strip().split(",")
#                         if len(parts) != 4:
#                             write_log(f"Invalid format in {filename}: {line.strip()}")
#                             print(f"Invalid format in {filename}: {line.strip()}")
#                             continue

#                         emp_id, name, email, salary = parts

#                         if not is_valid_email(email):
#                             write_log(f"Invalid email: {email} in {filename}")
#                             print(f"Invalid email: {email} in {filename}")
#                             continue
#                         if not is_valid_salary(salary):
#                             write_log(f"Invalid salary: {salary} in {filename}")
#                             print(f"Invalid salary: {salary} in {filename}")
#                             continue

#                         entry_key = (emp_id, email)
#                         if entry_key in seen_entries:
#                             print(f"Duplicate entry skipped:======================= {entry_key}")
#                             continue
#                         seen_entries.add(entry_key)
#                         cleaned_entry = [department, emp_id, name, email, salary]
#                         all_employees.append(cleaned_entry)
#                         departments[department].append({"emp_id":emp_id, "name":name, "email":email, "salary":salary})
#                         print(f"Added entry: {cleaned_entry}")

#             except FileNotFoundError:
#                 write_log(f"File not found: {filename}")
#                 print(f"File not found: {filename}")

#     except Exception as e:
#         write_log(f"Unexpected error: {str(e)}")
#         print(f"Unexpected error: {str(e)}")
   

#     with open(CLEANED_CSV, "w", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["department", "employee_id", "name", "email", "salary"])
#         writer.writerows(all_employees)
#     print(f"Written cleaned data to {CLEANED_CSV}")

#     write_log(f"Valid entries written: {len(all_employees)}")
#     print(f"Valid entries written: {len(all_employees)}")

#     # Write JSON
#     with open(JSON_FILE, "w") as jsonfile:
#         json.dump({"departments": departments}, jsonfile, indent=2)
#     print(f"Written JSON data to {JSON_FILE}")

#     # Create backups
#     create_backup()
#     print("Backups created.")
#     write_log("Processing complete. Backups created.")
#     print("Processing complete.")

# if __name__ == "__main__":
#     main()







import os
import json
import csv
import json
import shutil
from datetime import datetime

script_directory_os = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = "backup"
CLEANED_CSV = "all_employees_cleaned.csv"
JSON_FILE = "employees.json"
LOG_FILE = "log.txt"
DATA_DIR = os.path.join(script_directory_os,'data')



def validate_email(email):
    if "@" in email and "." in  email:
        return True
    else:
        return False

def validate_salary(salary):
    try:
        float(salary.replace('$',""))
        return True
    except ValueError: 
        return False
     
def log(message):
    with open('log.txt','a') as f:
        f.write(message)

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    shutil.copy(CLEANED_CSV, f"{BACKUP_DIR}/all_employees_cleaned_{timestamp}.csv")
    shutil.copy(JSON_FILE, f"{BACKUP_DIR}/employees_{timestamp}.json")

def main():
    departments = {}
    all_employees = []
    copy =set()
    
    try:
        
        files = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
        for filename in files :
            department_name = filename.replace(".txt","")
            departments[department_name] = []
            filepath = os.path.join(DATA_DIR, filename)
            try:         
                with open(filepath,'r') as f:
                    readLines = f.readlines()
                    log(f"the file is read {len(readLines)}")
                
                for line in readLines:
                    parts = line.strip().split(',')
                    if len(parts) != 4:
                        continue
                    emp_id, name, email, salary  = parts

                    if not validate_email(email):
                        log(f" in valid email please put valid")
                        continue
                    if not validate_salary(salary):
                        log(f" in valid salary please put valid salary")
                        continue
                    indentity = (emp_id,email)
                    if indentity in copy:
                        log(f"duplicate remove")
                        continue
                    copy.add(indentity)
                    cleaned_data = [department_name,emp_id,name, email,salary]
                    all_employees.append(cleaned_data)
                    departments[department_name].append({
                        "employee_id" :emp_id,
                        "name": name,
                        "email" : email,
                        "salary" : salary
                    })
            except FileNotFoundError:
                log(f"File not found: {filename}")
                print(f"File not found: {filename}")

    except Exception as e:
        log(f"Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")


    with open(CLEANED_CSV,'w') as f:
        writer = csv.writer(f)
        writer.writerow(['department','employ-id','name','email','salary'])
        writer.writerows(all_employees)
        log(f' all employies added :{len(all_employees)}')

    
    with open(JSON_FILE,'w') as f :
         json.dump({"department" : departments},f,indent=2)
        

              

                    
main()      
        

    