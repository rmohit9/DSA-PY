#instance Method

class Test:
    x=2
    def __init__(self,a,b):
        self.a=a
        self.b=b        
    def show(self):
        print(self.a,self.b)
    @staticmethod
    def f2():
        print("Hello")
    @classmethod
    def f3(cls):
        print(cls.x)
    

t1= Test(3,4)
t2= Test(5,6)
t1.show()
t2.show()
Test.f3()    #calling class method
Test.f2()    #calling static method

# o/p:  3 4
#       5 6
#       2
#       Hello
            
                           
  
    # #Instance Method- it should always have an argument 'self' with NO DECORATOR 
    # variable inside instance object is called instance variable
        # def f1(self):
        #     pass
    
    # #Static Method-It is your choice to have or dont have arguments but it should contain a decorator (@staticmethod) 
    # (variable inside the class object are called static variable)
        # def f2():
        #     pass
        # @staticmethod
    
    # #Class Method-It should contain atleast one argument along with the decorator (@classmethod)
        # def f3(cls):
        #     pass
        # @classmethod
    
    
class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.salary
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
e1= Employee()
e2= Employee(1,"Mohit",11100)
e1.setEmpid(1)
e1.setName("Harshal")
e1.setSalary(45000)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())

# o/p:  45000 Harshal 45000
#       11100 Mohit 11100