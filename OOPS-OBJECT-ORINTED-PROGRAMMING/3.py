# # class Property:
# #     def __init__(self,room):
# #         self.room =room

# # ob1 = Property("3")
# # print(ob1.room)


# class Student:
#     def __init__(self,name,roll):
#         self.name =name
#         self.roll =roll
#         self.institute = "PIAIC"

#     def get_addmission(self):
#         print(f'you have got successfully admision youur  roll is {self.roll}')

# ob1 = Student("mohamil",234)
# ob2 = Student("zain",2454)
# ob3 = Student("ESDFSDF",34534)
# print(ob1.name)
# print(ob1.get_addmission())

# class Course(Student):
#     def __init__(self,course,name,roll):
#         super().__init__(name,roll)
#         self.course_name =course
#         self.students = []

# cou1= Course("AI",'zaid','4500')
# # cou1.students.append(ob1)
# # print(cou1.students[0].name)
# print(cou1.name)



#  overriding --->
class Animal:
    def __init__(self,name,age):
       self.name = name
       self.age= age
    
    def make_sound(self):
        print("gurrr !")


class Dog(Animal):
    def __init__(self,name,age):
       self.name = name
       self.age= age
    
    def make_sound(self):
        print("bhaas!")

    
ob1= Dog("bil dog" ,2)
# print(ob1.make_sound())        




# *************************************************
#                ABSTRACTION
# *************************************************

# from abc import ABC, abstractmethod
# class BaseClass(ABC):
#     @abstractmethod
#     def method_1(self):
#          #empty body
#          pass

# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.engine_started = True


# ob34 =Car("honda","civics",2025)
# print(ob34.year)



# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        print("orint  the detail ..")
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")
# print(car1)
# Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()



class Bank(ABC):
    def __init__(self,name,number):
        self.name = name
        self.IBN_num =number

    @abstractmethod
    def security(self):
        pass

class Alhabib(Bank):
    # if  i will  not used msg so i can't access Bank class  you can check to commit the code above
    # 
    #  
    def security(self):
        print(f"you {self.name} bank  no is {self.IBN_num}") 

    # this fun never run without security func implementatation  beacause of abstract method       
    def normal(self):
        print(self.IBN_num)
    
alhabib =Alhabib("al-habeeb",42342342342342342)
alhabib.normal()





