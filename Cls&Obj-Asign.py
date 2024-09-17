#Q1:
class Person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
p1=Person()
p2=Person('Mohit',19)
p1.setName('Harshal')
p1.setAge(20)
print(p1.getName(),p1.getAge())
print(p2.getName(),p2.getAge())

        
class Circle:
    def __init__(self,radius=None):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return (3.14*self.radius**2)
    def getCircumference(self):
        return (2*3.14*self.radius)
    
c1=Circle()
c1.setRadius(3)
print("Radius is ",c1.getRadius())
print("Area is ",c1.getArea())
print("Circumference is ",c1.getCircumference())   



class Rectangle:
    def __init__ (self,length=None,breadth=None):
        self.length=length  
        self.breadth=breadth
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimensions(self):
        print("the length of the rectangle is {self.length} and breadth is {self.breadth}")
    def getArea(self):
        print("Area is {self.length}*{self.breadth}")
        