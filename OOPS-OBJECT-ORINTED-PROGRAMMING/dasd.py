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

# print(type(car),car.brand)
# print(type(truck),truck.brand)







# +++++++++++++++++++++++++++++++++++++++++++
#              Abstraction
# ++++++++++++++++++++++++++++


# Define a Car class with abstraction and idle stop engine feature
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False
        self._idling_time = 0
        self._traffic_signal = None

    # Expose a drive method without revealing internal mechanics
    def drive(self):
        if self._engine_status and self._traffic_signal == "green":
            print(f"You are driving a {self.brand} {self.model}.")
        elif self._traffic_signal == "red":
            print(f"You stopped at the red light in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            self._start_engine()
            print(f"You are driving a {self.brand} {self.model}.")

    # Expose a stop method to stop the car
    def stop(self):
        if self._engine_status:
            print(f"You stopped the {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

    # Expose a set_traffic_signal method to set the traffic signal
    def set_traffic_signal(self, signal):
        self._traffic_signal = signal
        if signal == "red":
            print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        elif signal == "green":
            print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
            if not self._engine_status:
                self._start_engine()

    # Internal method to start the engine (hidden from user)
    def _start_engine(self):
        self._engine_status = True
        self._idling_time = 0
        print("Engine started.")

    # Internal method to stop the engine if idling for 5 seconds (hidden from user)
    def _idle_stop_engine(self):
        import time
        print("Engine is idling...")
        for i in range(5):
            print(f"Idling time: {i+1} seconds")
            time.sleep(1)
            self._idling_time += 1
        if self._idling_time >= 5:
            self._engine_status = False
            print("Engine stopped (idle stop) to save fule.")


class ShopingMall:
    def basement_parking():
        car = Car('Toyata','Camri')
        car._start_engine()
    basement_parking()

   
class BMW(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start_engine(self):
        self._start_engine()
    def _start_engine(self):
        print("BMW engine is started")

bmw: BMW = BMW("BMW", "i5")
bmw.start_engine()

