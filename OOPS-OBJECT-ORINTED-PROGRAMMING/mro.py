class A():
    def greet(self):
        return("hello from A class")

class B(A):
    def greet(self):
        return("hello from B class")
    
class C(A):
     def greet(self):
        return("hello from C class")

class D(B,C):
    pass


d= D()
print(D.mro())
print(d.greet())


