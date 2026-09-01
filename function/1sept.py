# function  : 
"""
syntax : 

def function_name() :
    code  
call function_name 

4 type  : 

1. no arg  no return
2. no arg  with return
3. with arg  no return
4. with arg  with return

"""

# ex :1  no arg  no return 

"""def add():  # add ------> function  name  
    a=int(input("enter the  number  1: "))
    b=int(input("enter the  number  2: "))   # function  intialization  
    print("sum of two product is  : ",a+b)
    
add()
add()
add()
print("piyush  intelligent")
print("vishnu the GOD")
add()
"""

# parameter  :  function  declaration   
# argument  :  function  call ---->

# ex :2  with arg no return 

"""def add(a,b) :  # add function  name ,a,b ----> parameter
    print(a+b)

add(12,56)
add(12.90 ,45.90)
add("praincy","varma")
"""

# ex :3 no arg  with return 
"""def add():
    a=int(input("enter the  number  1: "))
    b=int(input("enter the  number  2: "))
    return a+b
print(add())
"""

# ex :4  with arg  with return

"""def add(a,b) :
    return a+b

print(add(23,78))
"""

# prime  number  using  function : 

def is_prime(n):
    count =0 
    for i in range(1,n+1):
        if n % i ==0 :
            count +=1
    if count ==2 :
        return True
    else :
        return False
    
print(is_prime(3))

# HW : amg , reverse , pelidrome ,twin ,perfect  using  function  . 