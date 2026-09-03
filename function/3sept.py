# *args : it takes only   number of arguments

"""def add(a,b=90) :
    return a+b
print(add(23.45,56))
print(add(23.45))
print(add(23.45,34))
"""

"""def add(*args):
    return sum(args)

print(add(1,2,3,4,5,6,7))
print(add(1,2,3,4,5,6,7,8,9,10))
print(add(23))
"""

# ex :2 

"""def n_sum(*bhavesh):
    sum =0 
    for i in bhavesh:
        sum +=i 
    return sum
print(n_sum(1,2,3,4,5,6,7,8,9,10))
print(n_sum(23,45))
print(n_sum(23))
"""

# ex :3 **kwargs : it takes any string and  number  both. 

"""
def d(**kwargs):   # dict  -----> items () ----> key value 
    
    for i ,j in kwargs.items():
        print(f"{i} : {j}")
d(name ="tisha" ,age =21 , hobby ="sleeping")
"""

# ex :4 menu driven  program calculator 

"""
CALCULATOR 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Moduls 
6. Floor Division
7. exit 


"""

"""def add(a,b):
    print("sum  of  two  numbers  is  ",a+b)

def sub(a,b):
    print("difference  of  two  numbers  is  ",a-b)

def mul(a,b):
    print("product  of  two  numbers  is  ",a*b)

def div(a,b):
    print("quotient  of  two  numbers  is  ",a/b)

def mod(a,b):
    print("remainder  of  two  numbers  is  ",a%b)

def floordiv(a,b):
    print("floor  of  two  numbers  is  ",a//b)
    
    
def menu():
    while True:
        print("CALCULATOR")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Moduls")
        print("6. Floor Division")
        print("7. exit")
        choice =int(input("Enter your choice "))
        
        if choice ==1:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            add(a,b)
        elif choice ==2:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            sub(a,b)
        elif choice ==3:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            mul(a,b)
        elif choice ==4:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            div(a,b)
        elif choice ==5:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            mod(a,b)
        elif choice ==6:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            floordiv(a,b)
        elif choice ==7:
            break
        else :
            print("Wrong choice")
menu()
"""
"""
1. number  1 ----> a=90 b=12  1   2  3   7 ---> enter the  new  number : 23 12   1 
"""

# local variable : 

"""def y() :
    a=9000    #  a local variable : accessible only inside the function
    print(a)
    
y()
print(a)  # local variable can't be accessed outside the function
"""
# gobal variable : accessible everywhere

"""
x=900 
def y() :
    print("inside  function  x value is  ",x)  # global variable accessible  inside function also 

y()
print("outside  function  x value is  ",x)  # x is accessible everywhere bcz  of  its global variable.
"""

# global variable can  modify using  global keyword :
"""x=900 
def y() :
    global x 
    x=7000
    print("inside  function  x value is  ",x)  

y()
print("outside  function  x value is  ",x)  
"""


# employees managment system
"""
1.add
2.delete
3.update
4.search
5.display
6.exit

"""

"""d1={}

def add():
    id=int(input("Enter id : "))
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    salary = int(input("Enter salary : "))
    d1[id] = [name,age,salary]
    print("employee added successfully")

def delete_emp(): 
    id =int(input("Enter id of employee you want  to delete : "))  # 101 
    if id in d1 : 
        del d1[id]
        print("employee deleted successfully")
    else :
        print("employee not found")
        
def update_emp():
    id =int(input("Enter id of employee you want  to update : "))  # 101 
    if id in d1 : 
        salary = int(input("Enter new salary : "))
        d1[id][2] = salary
        print("employee updated successfully")
    else :
        print("employee not found")
def search_emp():
    id =int(input("Enter id of employee you want  to update : "))  # 101 
    if id in d1 :
        print("name  : ",d1[id][0])
        print("age  : ",d1[id][1])
        print("salary  : ",d1[id][2])
    else :
        print("employee not found")
def display() : 
    
    
def menu() :
    
          
add()
add()
add()
print("before delete your employees are : \n",d1)
delete_emp()
print("after delete your employees are : \n",d1)
update_emp()
print("after update your employees are : \n",d1)
search_emp()
"""
"""
id    name   age  salary

102   vishnu 22   90000
103   prashant 23   80000
"""


 