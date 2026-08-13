"""
loop  : iteration   ----> repeation 

2 types of loop :

1. for loop  
2. while loop

syntax  for  loop:

for variable name in range (start,stop,step):
    print(variable name)

"""

# ex :1 print 1-100 

"""
for i in range(1,101):  # start ,stop 
    print(i,end= " ")
"""
# hw  2 print  a to z using  for loop . 

# ex :2 print 100 -1 

"""for x in range(100,0,-1):  # 100 99 
    print(x,end=" ")   # 100 99
"""    

# ex :3 print odd number from 1 to 100
"""
for i in range(1,101,2):  # start ,stop ,step size 2 
    print(i,end= " ")

for x in range(1,101,3):  # start ,stop ,step size 3 
    print(x,end= " ")
"""

# ex :4 print even number from 1 to 100

"""
for y in range(0,101,2) :  # 0 2   4  6  8 
    print(y,end= " ")
"""

# task  1 : print -10 to 30  using  for  loop  
# task :2 : print 30 to -30 using  for loop 

# prime  number  : 2 factors prime   ----> 1, number  itself
"""
4 factors : 1,2,4  -----> 3 facotrs ----> not  prime  
7 factors : 1,7  ----> 2 factors  ----> prime
99 factors :1,3,11,33,99 ----> 5 factors ----> not  prime  
19  factors : 1,19  ----> prime  

"""

"""n=int(input("enter the  number : "))  #4
count =0 

for i  in range(1,n+1):   #  4, 5 
    if n % i==0 :  #     if 4 % 4 ==0 
        count = count+1   # count =3

if count ==2 :  # 3==2
    print("it is  prime")
else :
    print("it is  not  prime")
"""

# ask user to enter the number and print the n natural number  sum. 
"""
input  : 5 
output  : n natural number sum is  : 15 

"""
"""n=int(input("enter the  number : "))   # 4 
sum =0 

for i in range(1,n+1) :  #  4 , 5
    sum =sum +i    # sum = 10
print("n natural number sum is  : ",sum)  # 1   3  6   10 
"""

"""
task : 1 ask user to enter the number and print the factorial of the number.
    input  : 5 
    output  : 1*2*3*4*5 =120 
    
task  :2 ask user to enter the number and  print  sum and  factorial  both  
    input  : 5 
    output  : n natural number sum is  : 15
               factorial of the number is  : 120
               

"""

