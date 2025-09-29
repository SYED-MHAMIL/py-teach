class CountCalls:
    def __init__(self,func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwds):
        self.call_count+=1
        print(f"Decorators: Call {self.call_count}  of {self.func.__name__}")
        print("arg" ,args ,"kwds= ",kwds)
        return  self.func(*args,**kwds)
    
@CountCalls
def say_hello(name,greet= "hello"):
    print(f'{greet}, {name}!')

say_hello("zain",greet= "Thanks")
say_hello("Mohamil",greet= "hello")




# ******************************************************************************
#                        Class decorator
# ******************************************************************************

def add_greeting(cls):
    def greet(self):
        return f'{self.__class__.__name__} ',self.name
    cls.greet = greet
    return cls  

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name
    
p1 = Person("mohamil") 
print(p1.greet())






# ******************************************************************************
#                       Property Decorator Example
# ******************************************************************************
class Person:
    def __init__(self,name):
        self._name= name
    @property
    def name(self):
        """GETTER FOR THE NAME """
        return self._name

    @name.setter
    def name(self,new_name):
        "SET THE NAME"
        if not isinstance(new_name,str):
           raise ValueError("Name Must be a string")    
        self._name = new_name


    
c1= Person("zain")
print(c1.name)        
c1.name= "CEO Mhmail"
print(c1.name)