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
# print(str(p1))





