class car:
    category="SUV"
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=car("Nexon",2024)
print(c1.category)
c1.display()

class add1:
    a=10
    b=20
    def addition(self):
        add=self.a+self.b
        print(add)
ad=add1()
ad.addition()
