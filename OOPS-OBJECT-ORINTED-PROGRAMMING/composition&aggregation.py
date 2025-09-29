# **********************************************************************
     #             COMPOSITION & AGREGAATION 
# **********************************************************************

# what is composition  ? 
# ans : composion is a "has-a" relationship where one object contains other  and the contained object's life cye is dependent on the container object , if the container  object is destroyed so contained object is also destroyed , it's a strong relationship , like a car and its engine ; the car run function without the engine, and engine is intrinsicall part of the car 

class Engine:
    def run_engine(self):
        return "running engine"


class Car:
    def __init__(self):
        self.engine = Engine()
car1 =Car()
# print(car1.engine.run_engine())
         


# **************************************************
#            Example #2               
# **************************************************

class Pages:
    def __init__(self,number):
        self.number = number 
        print(f"Page {self.number} created")
    
    def __del__(self):
                print(f"Page {self.number} destroyed")
    
    
class Book:
     def __init__(self,nums_pages):
        print(f"Book created")
        self.pages = [Pages(i) for  i in range(1,nums_pages+1)] 
     
     def __del__(self):
                print(f"****************  BOOK  destroyed ***********")
    
book1 = Book(3)
del book1
# print(book1.pages)



# ***   what is the difference b/w Inheritance and Composition and when to use Inheritance and when to use Composition?
# Inheritance is uesd where the class wants to nature of parents class and then modify  OR  extend the functionality of it .Inheritance will extend the functionality with extra features allows overriding of methods, but in the case of Composition, we can only use that class we can not modify or extend the functionality of it. It will not provide extra features. Thus, when one needs to use the class as it without any modification, the composition is recommended and when one needs to change the behavior of the method in another class, then inheritance is recommended.  

class Parent:
    def m1(self):
        print("Parent class method called")


class Child(Parent):
    def __init__(self):
        print("child class object created")
    
    def m2(self):
        print("Child class method called")

# c1 = Child()
# c1.m1()
# c1.m2()










# ****************************************************************

# What is Aggregation? (Weak Relationship)
# Aggregation is also a "has-a" relationship, but it represents a weaker association than composition. In aggregation, the contained object can exist independently of the container object. It's like a university and its departments; the university contains departments, but the departments can exist even if the university ceases to exist.


# ****************************************************************

class University:
     def __init__(self,name):
         self.name =name
         self.departments = []
    
     def addDeparment(self,depart):
         self.departments.append(depart.department)
         

class Department:
    def __init__(self,department):
        self.department = department 

depart = Department("AI ENGINEER")
standford  = University("Standford")
standford.addDeparment(depart)
# print(fast.departments)



