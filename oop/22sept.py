# polymorphism  :  many forms  same  methods behavior  different  parameters. 
"""
1. method overloading 
2. method overriding 

"""

# ex :1 method overloading

"""class calculator :
    def add(self,a,b,c=90,d=89):
        return a+b+c+d
c=calculator()
print(c.add(12,90))
print(c.add(1,2,3))
print(c.add(1,2,3,4))

"""

# ex :2 
"""class calculator :
    def add(self,*args):
        return sum(args)
    
    
c=calculator()
print(c.add(1,2,3,4,5,6,7,8,9,10))
print(c.add(10,20))
print(c.add(10))
"""

# ex :3 method overriding
"""
class animal : 
    def sound(self):
        print("animal  is  sounding")

class dog(animal):
    def sound(self):
        print("dog  is  barking")
        
class cat(animal):
    def sound(self):
        print("cat  is  meowing")
        
d=dog()
d.sound()

c=cat()
c.sound()

"""

# abstraction  :  to hide the details of the implementation and only show the essential features

"""
ex : car ----> strearing , accelerating , braking, cluch 
    ATM machine  : 
    
1. abstract class : no  object created 
2. abstract method : define  ----> no  intialized 
3. lib : ABC -----> abstract base class  from abc import ABC 
"""

"""from abc import ABC, abstractmethod

class vehicle(ABC) :
    def __init__(self,type):
        self.type = type
    
    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod   # decorator
    def stop(self):
        pass 
    
class car(vehicle):
    def __init__(self,type,speed):
        vehicle.__init__(self,type)
        self.speed = speed
        
    def start(self):
        print("car  is  starting")
        print("speed  is  : ",self.speed)
        
    def stop(self):
        print("car  is  stopping")
        print("car max speed  is  : 250.")
        
c=car("four wheeler",200)
c.start()
c.stop()


"""

# class method  : 
"""
1. can be modify  
2. first argument  is  cls 

"""

"""class student : 
    clg_name ="Nirma University"

    @classmethod   # decorator  
    def display(cls,new_name):
        cls.clg_name = new_name
        print("clg_name  is  : ",cls.clg_name)
        
print("old clg name is  : ",student.clg_name)

student.display("AU")
print("new clg name is  : ",student.clg_name)

"""

# static method  :
"""
1. works  like  normal  function 
2. not  modify  
3. not  first  arg as self  or  cls 
"""

class maths :
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
            return a-b
        
m=maths()
print(m.add(10,20))
print(m.sub(34,12))