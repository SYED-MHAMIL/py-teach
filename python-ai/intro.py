class Person: # Class Person (source code/blue print of an object at runtime)
        def __init__(self, name: str, age: int): # initilizer or constructor which is responsible to create Object in memory at runtime
            self.name = name           # Pereson attibute
            self.age = age             # Pereson attibute

        def greet(self): # Person Class method greet()
            print(f"Hello, my name is {self.name} and I am {self.age} years old.") # Print/Output to console/terminal

# Lets create a Person object in memory
person: Person = Person("Arif Rozani", 20)

person.greet() # Lets call Person Object's greet method


import dis

# what does dis work ?
# ans ) dis by the way works to check how to program run and what is happenning behind the scene ..




b =dis.dis(Person)
print(b)