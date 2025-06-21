class Car:
    def __init__(self,branduser,modeluser):
       self.brand = branduser
       self.model = modeluser

    def fullName(self):
        return f"{self.brand} {self.model}"    

# new_Car = Car("Toyota","corolla")
# print(new_Car.fullName())



    
# CERATE AN ELCTRICCAR CLAAS THAT INHERITS THE CARS and add barttery size


# wrong
# class Electric_car:
#     new_Car = Car()
#     def __init__(self,brand,model,battery_size):
#         new_Car = Car(brand,model)
#         new_Car.self.battery_size = battery_size
#         return new_Car

# el =Electric_car("Meharan","vx","220 Volt")
# print(el)




# CORRECT  WAY  TO  INHERITS CLASS 
#  ==================    INHERITANCE   ==========

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


# tasla = Electric_car("tesla","Cybertrack","10000 volts")

# print(tasla.fullName())
        


#  ==============  POLYMORPISM  ===========



