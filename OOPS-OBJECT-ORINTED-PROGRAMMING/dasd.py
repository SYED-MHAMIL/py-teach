# class Point:
#     def __init__(self,x,y):
#         self.x =x
#         self.y=y
#     def __add__(self,other):
#        add =Point(self.x+other.x,self.y+other.y)
#        return add
#     def __str__(self):
#         return(f"point({self.x},{self.y})")
        
#     @staticmethod
#     def d():
#         return "Static"

# p1=Point(1,3)
# p2 =Point(2,4)
# newOp = p1+p2
# print(newOp)






class Point:
    def __init__(self,x,y):
        self.x =x
        self.y=y
    def __add__(self,other):
       return self.x+other.x,self.y+other.y # wrong
    #  but __str__ does not work because this want to a oject itself
    def __str__(self):
        return(f"point({self.x},{self.y})")
        
    @staticmethod
    def d():
        return "Static"

p1=Point(1,3)
p2 =Point(2,4)
newOp = p1+p2
# print(newOp)






# **************************************************************************************
# **************************************************************************************

# **2.__str__ vs __repr__ - Toy Labels**
#   - __str__: Friendly display (for customers)
#   - __repr__: Exact specs (for warehouse staff)

# **************************************************************************************
# **************************************************************************************


class Puzzle:
    def __init__(self,pieces):
        self.pieces = pieces
    def __str__(self):
            return f"Puzzle with {self.pieces} fun pieces!"

    def __repr__(self):
        return f'pieces{self.pieces}'
        

p1 = Puzzle("100")
# print(str(p1))''













# If I can access class stuff using the class name, why bother with cls?


class Animal:
     spices = "dog"
     @classmethod
     def make(cls):
         return cls() # 'cls' will be whichever calls the 'cls'

class Lion(Animal):
    spices ='lion'

sp1=Animal()
animal= sp1.make()
print(animal)

sp2 = Lion()
animal2 = sp2.make()
print("this is calls =>>>>>>> ",animal2)

# ✅ Because we used cls(), it returned a Dog instance, even though the method was defined in the Animal base class.




# ======================================================================================
# #   a real-world analogy showing the difference between using cls (dynamic) vs using a hardcoded class name (static) when creating instances.

# # Analogy: Vehicle Factory ======================================================================================




class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    @classmethod
    def create(cls,brand):
        return cls(brand)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

c = Car("Toy")  
car = c.create("Toyata")
truck = Truck.create('Ford')

print(type(car),car.brand)
print(type(truck),truck.brand)




#  if i will pass static clas name what will be happened ?

class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    @classmethod
    def create(cls,brand):
        return Vehicle(brand)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

c = Car("Toy") 
car = c.create("Toyata")
truck = Truck.create('Ford')

print(type(car),car.brand)
print(type(truck),truck.brand)