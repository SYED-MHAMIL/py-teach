class Point:
    def __init__(self,x,y):
        self.x =x
        self.y=y
    def __add__(self,other):
       return Point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return("hello syed mohamil")
p1=Point(1,3)
p2 =Point(2,4)
newOp = p1+p2
print(newOp)   