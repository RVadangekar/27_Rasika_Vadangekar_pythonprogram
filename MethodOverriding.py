from math import pi
class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*self.r*self.r
r1=rect(5,3)
c1=circle(10)
print("area of rectangle: ",r1.area())
print("area of circle: ",c1.area())
for common in (r1,c1):
    print("area is: ",common.area())
