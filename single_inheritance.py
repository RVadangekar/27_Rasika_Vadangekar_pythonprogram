class student:
    def input(self,name,roll,PRN, address):
        self.name=name
        self.roll=roll
        self.PRN=PRN
        self.address=address
    def display(self):
        print("name: ",self.name)
        print("roll: ",self.roll)
        print("PRN: ",self.PRN)
        print("address: ",self.address)

class CSE(student):
    def setMarks(self,marks):
        self.marks=marks
    def setSubject(self,subject):
        self.subject=subject
    def display(self):
        print("name: ",self.name)
        print("roll: ",self.roll)
        print("PRN: ",self.PRN)
        print("address: ",self.address)
        print("Marks: ",self.marks)
        print("subjects: ",self.subject)

s1=CSE()
s1.input("rasika",26,"EN21120202","kolhaput")
s1.setMarks(100)
s1.setSubject("python")
s1.display()
        
        
