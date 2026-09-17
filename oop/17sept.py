# python  : object  oriented programming language 

"""
class :  blue print of object
object :  intstance of class

ex : 

fruits     ------> class 
     apple , kiwi , mango ,chiku  -----> object 

syntax : 

class  name :
    code 
object =class_name()
"""
# ex :1 
"""class student:   # student  class name  
    print("its  student class")   # intializer
    print(" student class : harshita , vishnu ,praincy,arzu,smit,roshni")
    
s=student()   # s object of class student
"""


# class type and  attributes  : 
"""
1. public class : accessible from anywhere
2. private class : accessible only from inside the class
3. protected class : accessible only from inside the class and its subclasses

"""

# ex :2   example  of  class and  attributes

"""
class student :   # class name  ----> student
    name = "harshita"   # name  age  city ----> class attributes
    age =20 
    city = "ahmedabad"
    
s=student()
print("name is  : ",s.name)  # access class attributes though object
print("age  is  : ",s.age)
print("city is  : ",s.city)
"""

# ex :3  example  of  class and  attributes with function  : 

"""class vehicle : 
    name = "BMW"
    model = "X5"
    seating_capacity = 6

    def display(self,city):  # self ----> keyword , class ----> function  , attribute ----> access 
        print("name  is  : ",self.name)
        print("model  is  : ",self.model)
        print("seating  capacity  is  : ",self.seating_capacity)
        print("city  is  : ",city)
        
v=vehicle()
v.display("mumbai")
"""

# ex :4  public : 

"""class student :   # class name  ----> student
    name = "harshita"   # name  age  city ----> class attributes ----> public 
    age =20 
    city = "ahmedabad"
    print("name is  : ",name) 

s=student()
print("name is  : ",s.name)  # access class attributes though object
print("age  is  : ",s.age)
print("city is  : ",s.city)
s.name  = "vishnu"
s.age = 21
s.city = "mumbai"

print("after  update name  age and  city  : \n")
print("name is  : ",s.name)
print("age  is  : ",s.age)
print("city is  : ",s.city)

"""

# ex :5  private :

"""class student : 
    name = input("enter  name  : ")  # name  ,  city  ----> public 
    city = input("enter  city  : ")
    __age = input("enter  age  : ")  # __age ----> private 

    # print("age is  : ",__age)
    
    def display(self):
        print("age is  : ",self.__age)
    
    
s=student()
print("name is  : ",s.name)
print("city is  : ",s.city) 
# print("age is  : ",s.__age)    # outside class not  accessible bcz  of  private
# s.__age =18   # not  modify  private  attribute
s.display()
"""

# ex :6  protected :

"""class vehicle : 
    name = "BMW"   # name  seating_capacity  ----> public
    _model = "X5"  # _model ----> protected
    seating_capacity = 6
    
class car(vehicle): 
    def display(self) :
        print("name  is  : ",self.name)
        print("model  is  : ",self._model)
        print("seating  capacity  is  : ",self.seating_capacity)
        
c=car()
c.display()
"""

# constructor :
"""
definition  : automatically called when object is created. 

syntax :
    def __init__(self,arg1,arg2,...,argn):

1. __init__  is  constructor/special method

"""

# ex :7  defualt constructor

"""
class student : 
    def __init__(self):
        print("default  constructor  called")
        print("student  class  created")

s=student()

"""

# ex :8  non -parameterized constructor

"""class student : 
    def __init__(self):
        self.name  ="smit"
        self.age = 20
        self.city = "mumbai"
        print("non -parameterized  constructor  called")
        print("student  class  created")
        print("student  class  created")

s=student()
print("name is  : ",s.name)
print("age  is  : ",s.age)
print("city is  : ",s.city) 
"""

# ex: 9 parameterized constructor

class student :
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        
    def display(self):
        return f"name is  : {self.name} , age is  : {self.age} , city is  : {self.city}"

s=student("harshita",20,"mumbai")
s1=student("vishnu",21,"kerala")
s2=student("priyanka",22,"delhi")

for i in [s,s1,s2]:
    print(i.display())