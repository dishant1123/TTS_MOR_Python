"""
4 main pillar of oop :

1. inheritance  : derived class  access the  base class properties and methods
    type  : 
    1.single  inheritance
    2.multiple  inheritance
    3.hierarchical  inheritance
    4.multi level  inheritance
    5.hybrid  inheritance
    
2. polymorphism  : many  forms  same  methods name  different  parameters / behavior
3. encapsulation : bundling data (attributes) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to some components to protect the internal state
    method : 
        1. get  method 
        2. set  method
4. abstraction :  to hide the details of the implementation and only show the essential features

    method  : 
        1. abstract  method
        2. abstract  class

"""
# ex : inheritance   ----> 1.single  inheritance

"""
class student : 
    name  ="harshita"
    age =20 
    
class clg(student):
    def display(self):
        print("name  is  : ",self.name)
        print("age  is  : ",self.age)
        
c=clg()
c.display() 
"""

# ex  :using constructor  in  derived class

"""class student : 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class clg(student):
    def __init__(self,name,age,clg_name):
        self.clg_name = clg_name
        student.__init__(self,name,age)
        
    def display(self):
        print("name  is  : ",self.name)
        print("age  is  : ",self.age)
        print("clg_name  is  : ",self.clg_name)
        
c=clg("harshita",20,"AU")
c.display()
"""

# ex :2 
"""
multi level  inheritance   vs    multiple inheritance

class a                            class a 
class b(a)                         class b
class c(b)                         class c(a,b)

"""

# multi level : 

"""class employees : 
    name ="ganpat"
    salary =30000 
    
class manager(employees):
    m_name ="vishnu"
    m_salary =80000
    
    def display(self):
        print("employee  name  is  : ",self.name)
        print("employee  salary  is  : ",self.salary)
        print("manager  name  is  : ",self.m_name)
        print("manager  salary  is  : ",self.m_salary)

class CEO(manager):
    c_name ="smit"
    
    def display(self):
        print("employee  name  is  : ",self.name)
        print("employee  salary  is  : ",self.salary)
        print("manager  name  is  : ",self.m_name)
        print("manager  salary  is  : ",self.m_salary)
        print("CEO  name  is  : ",self.c_name)
        
c=CEO()
# c.display()

m=manager()
m.display()
"""

#ex : hirearchical inheritance


"""class vehicle :
    type ="two wheeler"
    
class bike(vehicle):
    company = "honda"
    model = "shine"
    
    def display(self):
        print("type  is  : ",self.type)
        print("company  is  : ",self.company)
        print("model  is  : ",self.model)

class bicycle(vehicle):
    company = "yamaha"
    model = "p1"
    
    def display(self):
        print("type  is  : ",self.type)
        print("company  is  : ",self.company)
        print("model  is  : ",self.model)
        
b=bike()
b.display()

by=bicycle()
by.display()
"""

# ex : hybrid inheritance : combination  of  one  or more  than  one  inheritance
"""
class a 
class b(a)
class c(b)
class d(b,c)

 its  combination of multiple inheritance and multi level 
"""

"""
encapsulation :bundling data (attributes) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to some components to protect the internal state
    method : 
        1. get  method  : data get 
        2. set  method  : modify data
"""

# ex :1 

class student : 
    name ="harshita"
    __age =20    # private
    __salary =90000
    
    def get_method(self):  
        return f"age is  : {self.__age} , salary is  : {self.__salary}"

    def set_method(self,new_age):
        self.__age = new_age
    
    def set_salary(self,new_salary):
        self.__salary = new_salary

s=student()
print("before using  set method  : \n")

print("name is  : ",s.name)
print(s.get_method())

print("after using  set method  : \n")
s.set_salary(100000)
s.set_method(22)
print(s.get_method())

