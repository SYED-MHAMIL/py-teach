# Read multiple text files from a given directory (data/) where each file represents a department's employee records.
# Each file is named like: hr.txt, engineering.txt, marketing.txt
# Each line of a file has format: employee_id,name,email,salary
# Clean and validate the data:
# Remove duplicates.
# Ensure email format is valid.
# Filter out entries with salary not being a valid number.
# Store cleaned data into a single file called all_employees_cleaned.csv.


# Convert the final CSV into a JSON file named employees.json with the following structure:


# {
#   "departments": {
#     "hr": [...],
#     "engineering": [...],
#     "marketing": [...]
#   }
# }

# Add logging of the process to a log.txt file, including:

# Number of lines read.
# Number of valid entries.
# Errors encountered (if any).

# Implement exception handling for:
# File not found
# Incorrect data format


# Bonus Task:
# Create a backup of the cleaned CSV and JSON files in a folder named backup/ with a timestamped filename.





def checkEmail(email):
    if "@gmail.com" in email:
        return True
    else:
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
            data =data_one.read()
            print(data)
    except FileNotFoundError as e:
         print(f"ERROR: {e}")
          

    
    # for i in data.split(","):
    if checkEmail(data):
             try:
                  with open('all_employees_cleaned.csv','r') as extistfile:
                        existanceData = extistfile.read()
             except:
                   existanceData=[]
                

    try:
       if not data in existanceData:
            with open("all_employees_cleaned.csv","a" if existanceData else "w") as f:
                    if existanceData:
                         f.write(f"\n{data}")
                    else:
                         f.write(data)
                                          
    except:
         print("ad")
                   
              
         
        
         


        




