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
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        while True :
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
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                add(a,b)
            elif choice ==2:
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                sub(a,b)
            elif choice ==3:
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                mul(a,b)
            elif choice ==4:
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                div(a,b)
            elif choice ==5:
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                mod(a,b)
            elif choice ==6:
                # a=int(input("Enter first number "))
                # b=int(input("Enter second number "))
                floordiv(a,b)
            elif choice ==7:
                print("enter the number number  : ")
                break
            elif choice ==8:
                break
            else :
                print("Wrong choice")
        # sure =input("Do you want to continue (y/n) : ")
        # if sure =='Y':
        #     break
        # else :
        #     print("Wrong choice")
        break 
menu()
"""

# recursive function:function  call itself . 

"""
factorial : 5!   ----->120 
n * (n-1 )!   -----> 5 * (5-1) !  ----> 5 * 4!  ---->120 
"""

# normal function  : 

"""def facto(n):
    fact =1 
    for i in range(1,n+1):
        fact *=i
    return fact

print("factorial of 5 is ",facto(5))
"""
# recursive function :

"""def facto(n):  #  
    if n==1 :   #  1==1 
        return 1    # 1 
    else :
        return n * facto(n-1)  # 2 * facto(1)
    
print("factorial of 5 is ",facto(5))

"""

# n natural number sum  :  
"""
5 -----> 1+2+3+4+5 =15     -----> n + n(n-1)
"""
"""def n_sum(n) :
    if n==1 :
        return 1 
    else :
        return n + n_sum(n-1)
print(n_sum(5))
"""

# fabonacci seris  : 
"""
The Number PatternStarts with 0 and 1 (or sometimes 1 and 1).
Add the first two numbers to get the next: 0 + 1 = 1.Add the next pair: 1 + 1 = 2, then 1 + 2 = 3.The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 

FormulaWritten as a rule: \(F_n = F_{n-1} + F_{n-2}\)Each term (\(F_{n}\)) equals the sum of the step before it (\(F_{n-1}\)) and two steps before it (\(F_{n-2}\)).

"""

# using  while/for    : 

"""n=int(input("enter the number : "))
a=0
b=1
for i in range(n+1) :   # 11   ---->3
    print(a,end=" ")   # 0 1 1 2
    c=a+b               # c=a+b   --->c =3  
    a=b                  # a=b    ---->a=2  
    b=c                  # b=c   ----> b=3
"""

# using  recursive function :

"""def fibonacci_seris(n) :  # 10   55
    if n==0 :
        return 0 
    if n==1 :
        return 1
    else :
        return fibonacci_seris(n-1) + fibonacci_seris(n-2)
    
for i in range(11) :
    print(fibonacci_seris(i))
"""
# lambda function  : one  liner function ,its also called as anonymous function.

"""
syntax : 

lambda arg : expression
"""
# ex :1 
"""def add(a,b) :
    return a+b
print(add(23,45))

result =lambda a,b : a+b 
print(result(120,56))
"""

# ex :2 

"""def big(a,b) :
    if a>b :
        print("a is  big")
    else :
        print("b is  big")
big(12,56)

a =lambda x ,y : print("x is big") if x >y else print("y is big")
a(120,56)
"""

# ex :3 

"""def loop_in(n):
    for i in range(n+1):
        print(i,end=" ")
loop_in(5)
      
        
l =lambda x : [print(i,end=" ") for i in range(x+1)]
l(23)
"""

# ex :4 

"""result =lambda x : len(x)
print(result("hello"))
print(result((23,45,67,89,450)))
print(result([1,2,3,4,5,6,7,8,9,10]))
print(result({"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}))
"""

# filter : filter out the elements that satisfy the condition

l1 =[1,2,3,4,5,6,7,8,9]
"""odd=[] 
even=[] 

for i in l1 : 
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i)
print("odd",odd)  # [1,3,5,7,9]
print("even",even)  # [2,4,6,8]
"""

"""
r=list(filter(lambda x :x  % 2==0 ,l1))
r1=tuple(filter(lambda x :x  % 2==1 ,l1))
print(r)
print(r1)
"""

# map : map the elements to some other element its given a new list. 

"""l1 =[2,4,8,9,12]
square =[] 
for i in l1 :
    square.append(i**2)
print(square)  # [4,16,64,81,144]

r=list(map(lambda x :x ** 2 ,l1))
print(r)
"""

# filter the  pelindrome string  : 

l1 =["java","python","php","c","HTML","CSS","JS"]
"""peli =[] 

for i in l1 :   # java
    if i == i[ : : -1] :  # java = avaj
        peli.append(i)
print(peli)

"""
result =list(filter(lambda x : x ==x[::-1] ,l1 ))
print(result)