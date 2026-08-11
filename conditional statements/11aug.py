# conditional  statement : 
"""
if else  syntax : 

if (condition):
    print()
else :
    print()

"""

# ex :1 ask user to enter the age and check whether it is  eligible  for  voting  or  not. 

"""age =int(input("enter the age : "))

if age >=18 :
    print("eligible  for voting.")
else :
    print("not eligible  for voting.")
"""    

# ex : 2 ask user to enter the  2 number and  check which number is  big. 

"""
a=int(input("enter the  number 1 : "))
b=int(input("enter the  number 2 : "))

if a>b :
    print(" a is  big")
else :
    print(" b is  big")
"""

# ex :3 check the number is  even or odd.

"""
num =int(input("enter the  number : "))
if num % 2==0 :    # modulas operator  :  reminder 
    print("even")
else :
    print("odd")
"""

# ex :4 ask user to enter the number  and check number  is  divisible by 5 or not. 

"""num =int(input("enter the  number  : "))
if num % 5 ==0 :
    print("divisible by 5 ")
else :
    print("not divisible by 5 ")
"""    

# ex :5 nested if :
"""
if con :
    print() 
elif con :
    print()
elif con :
    print()
else :
    print()
"""
 

"""a=int(input("enter the  number 1 : "))  # 23
b=int(input("enter the  number 2 : "))   #89

if a>b :
    print(" a is  big")
elif b>a :
    print(" b is  big")
else :
    print(" same")
"""

# ex :6 ask user to enter the number and check whether number is div by  5 or 11 or both. 
"""
input  : 55    
output  : num is  div by 5 and 11  
"""

"""num =int(input("enter the  number : "))

if num % 5 ==0 and num % 11==0 :
    print("num is  div by 5 and 11 ")

elif num % 5==0 :
    print("num is  div by 5 ")

elif num % 11==0:
    print("num is  div by 11 ")

else :
    print("num is  not div by 5 and 11 ")
"""

# ex :7 ask user to enter the number and check whether number is div by  3 or 11 or both. 
"""
input  : 33  
output  : num is  div by 3 and 11  
"""

# ex :8 ask user to enter the  3 subject marks calculate the  percentage and based on percentage given the grade. 
"""
percentage     grade 
90+            A+ 
80-90          A 
70-80          B+ 
60-70          B
50-60          C+ 
40-50          C
below 40       Fail 
"""
"""
maths =int(input("enter the  maths  marks : "))  # 90
english =int(input("enter the  english  marks : ")) # 89
computer =int(input("enter the  computer  marks : "))#95
# 90 +89 +95  *100 /300   ------> percentage 

percentage = (maths+english+computer)/3
print("percentage  : ",percentage)    # 90

if percentage >=90 :
    print("Grade : A+")
elif percentage >=80  and percentage <90 :
    print("Grade : A")
elif percentage >=70 and percentage <80 :
    print("Grade : B+")
elif percentage >=60 and percentage <70 :
    print("Grade : B")
elif percentage >=50 and percentage <60 :
    print("Grade : C+")
elif percentage >=40 and percentage <50 :
    print("Grade : C")
else :
    print("Grade : Fail")
"""

# ex :10  ask user to enter the  basic  salary  and calculate the gross salary. 
"""
gross salary  = basic salary + HRA +DA 

HRA = basic salary *percent 
DA = basic salary *percent

range           HRA       DA 
0-10000         25%       30% 
10001 -20000    35%       40% 
above 20000     40%       50%

hint  : 

user =5000   ------> basic salary  
HRA =basic salary * 0.25  -----> 9000 *0.25  ----> 2250 
DA = basic salary * 0.3   -----> 9000 *0.3   ----> 2700

gross salary = basic salary + HRA +DA   ----> 9000 + 2250 +2700  ----> 13950
"""


