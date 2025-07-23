# *************************************************
#                 __DEL__ method
# *************************************************


# class Car:
#     # Parameterized constructor
#     def __init__(self,brand,model):
#         self.brand =brand
#         self.model =model
    
#     def __del__(self):
#         print("delete hogaya gehr jao")
#         del self

# # Create an object of the Car class
# my_car = Car("Toyota", "Corolla")
# # Explicitly delete the object (triggers the destructor)
# # del my_car  # Output: The Toyota Corolla has been destroyed.
# print(my_car.brand)






# *************************
#       fle example
# *************************

# import os

# class TEmpFile:
#     def __init__(self,filename):
#         self.filename = filename
#         with open(self.filename,'w') as f:
#             f.write("hi i am agentic ai enginnner")
    
#     def __del__(self):
#         print(f"your file is {self.filename} to be destroyed")
#         os.remove(self.filename)


# file =TEmpFile('billion.txt')
# print(file.filename)
# del file
# # print(file.filename)



# class FileHandler:
#     def __init__(self, filename):
#         self.file = open(filename, 'w')
#         self.file.write("Some initial data")
#         print("File opened and written to")

#     def __del__(self):
#         print("Closing file")
#         self.file.close()

# # Creating a FileHandler object
# file_handler = FileHandler('example.txt')

# # Deleting the object explicitly (calls __del__ method)
# del file_handler

#*********************************************


class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def full_name(self):
        return  print(f'the car brand is {self.brand} {self.model}')
    

class Elec:
    def __init__(self,b,m):
        self.car=Car(b,m)
    def get_Car_dec(self):
        print(f' {self.car.full_name()}')

    #❌ Not recommended, still accessible

e =Elec('d','sdsa')
print(e.get_Car_dec())

        