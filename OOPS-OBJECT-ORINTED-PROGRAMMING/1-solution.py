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

# class Electric_car1(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size


# tasla = Electric_car1("tesla","Cybertrack","10000 volts")

# print(tasla.fullName())







# ***********************************************************8
#                    Encapsulation  
# ***********************************************************8

# class Electric_car(Car):
#     def __init__(self,brand,model,battery_size):
#         self.__brand =brand
#         self.model = model
#         self.__battery_size = battery_size
    
#     # EXAMPLE
#     def get_brand(self):
#         print(self.__brand +"!")
#     # setter
#     def set_brand(self,brand):
#         self.__brand= brand
        








# more elegent approash with decorator


# class Electric_car(Car):
#     def __init__(self,brand,model,battery_size):
#         self.__brand =brand
#         self.model = model
#         self.__battery_size = battery_size
    
#     @property
#     def brand(self):
#         print(self.__brand +"!")
#     @brand.setter
#     def brand(self,brand):
#         if brand:
#             self.__brand= brand
#         else:
#             print("Brand cannot be empty")


# e1=Electric_car('honda','civic','450 kg')
# print(e1.brand)
# e1.brand= "tesla"
# print(e1._Electric_car__brand)





# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  What is @property?
# @property is a built-in decorator in Python used to define getter, setter, and deleter methods while allowing attribute-like access to methods.
# It makes methods behave like attributes, enhancing readability and encapsulation.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++




class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        self.__brand =brand
        self.model = model
        self.__battery_size = battery_size
    
    @property
    def brand(self):
        return getattr(self,'_Electric_car__brand','brand notfound')
    @brand.setter
    def brand(self,brand):
        if brand:
            self.__brand= brand
        else:
            print("Brand cannot be empty")
    @brand.deleter
    def brand(self):
        del self.__brand


e1=Electric_car('honda','civic','450 kg')
print(e1.brand)
e1.brand= "tesla"
# del e1.brand
print(e1.brand)




# +++++=+++++++++++++++  if  yo u want to dont use to decorator  in opps so we can write     +++++++++++++++++++++++


# class Elec():
#     def __init__(self,size):
#         self.__size =size
    
#     def get_size(self):
#         print(self.__size)
    
#     def set_size(self,size):
#         self.__size =size
    
#     size =property(get_size,set_size)
           
# ob1=Elec("450 volt")

# print(ob1.size)


# ✅ However, if you want to create your own version of @property, you can write a custom descriptor, but it's advanced.



# ******************************************************
#   if you want to own decorader for setter or getter 
# ********************************

class dec:
    def __init__(self, func):
        self.getter = func
        self.setter_func = None
        self.deleter_func= None

    def __get__(self, instance, owner):
        return self.getter(instance)
    
    def setter(self,setter_fun):
        self.setter_func = setter_fun   
        return self
    
    

    def __set__(self,instance,value):
        if self.setter_func is None:
           raise AttributeError("no setter defined")
        self.setter_func(instance,value)
           
    def deleter(self,deleter_func):
        self.deleter_func=deleter_func
        return self
    
    def __delete__(self,instance):
        if self.deleter_func is None:
           raise AttributeError("no deleter defind") 
        self.deleter_func(instance)
        






# class Electric_car(Car):

#     def __init__(self,brand,model,battery_size):
#         self.__brand =brand
#         self.model = model
#         self.__battery_size = battery_size
    
   
#     @dec
#     def brand(self):
#         return self.__brand+"!"
    
#     @brand.setter
#     def brand(self,brand):
#         if brand:
#             self.__brand= brand
#         else:
#             print("Brand cannot be empty")
    
#     @brand.deleter
#     def brand(self):
#         del self.__brand


# e1=Electric_car('honda','civic','450 kg')
# print(e1.brand)
# e1.brand="Tesla"
# print(e1.brand)
# del e1.brand
# print(e1.brand)




