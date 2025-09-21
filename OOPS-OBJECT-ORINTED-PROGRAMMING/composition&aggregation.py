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
print(car1.engine.run_engine())
         











# ****************************************************************

# What is Aggregation? (Weak Relationship)
# Aggregation is also a "has-a" relationship, but it represents a weaker association than composition. In aggregation, the contained object can exist independently of the container object. It's like a university and its departments; the university contains departments, but the departments can exist even if the university ceases to exist.


# ****************************************************************


