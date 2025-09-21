class Bakery:
    type  = "cake" 
    def __init__(self,flavor,price):
        self.flavor  = flavor
        self.price = price


cake =  Bakery("choco",100)
print(cake.type)
cake2 = Bakery("strawberry", 400)
Bakery.type = "pastry"
print(cake.type)
print(cake2.type)
            
