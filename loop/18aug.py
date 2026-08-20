# perfect number  , amg  number ,  reverse number  , pelidrome  number , twin number  : 

# while  loop : 
"""
syntax : 

i = intial value

while conditon :
     print()
     inc/dec 

"""

# ex :1  1-100 
"""
i=1               # i= 1 
while i <=100 :   # 101< =100
    print(i,end=" ")   # 1 2 3 ...100    
    i = i+1         # i= 101
"""

# ex :2 100-1 
"""
i=100      # i=100 
while i >=1 :    # 99 >=1 
    print(i,end=" ")   #100 99  
    i =i-1     # 99

"""

# perfect number  : 
"""
6 factors : 1,2,3,6
sum  =1+2+3 =6    ------> perfect number 

28 factors : 1,2,4,7,14,28 
sum = 1+2+4+7+14  ====>28 perfect number 

100 factors : 1,2, 4,5,10,20,25,50,100
sum = 1+2+4+5+10+20+25+50   ===> 118  not  perfect number  
 
"""
"""n=int(input("enter the  number : "))  #6
sum =0 

for i in range(1,n) :   # 5 ,6 
    if n % i==0 :    #  if 6 % 5 ==0  
        sum = sum +i  # sum = 6
        
if sum ==n :   # 6 == 6 
    print("it is  perfect number")
else :
    print("it is  not  perfect number")
"""

# reverse number  : 
"""
n=123 
output  : 321 

logic :  rev =0 
r = n %10   -----> r = 1 % 10 =  1    
rev = rev *10 +r   ------>rev =321  
num = num // 10    ------> num =1  // 10 =0     
"""

"""n=int(input("enter the  number : "))  #123
rev =0 
while n >0 :  # 0 > 0 
    r=n %10    # r = 1 %10 =1 
    rev =rev *10 +r  # rev = 321 
    n = n // 10   # n = 1 //10 = 0 

print("reverse number is  : ",rev)
"""

# amg number  : 
"""
153 : 
digit = len(str(153))  ------>3 

logic : 

1 **3    5**3   3**3 
1        125     27  
sum = 1+125+27   = 153 =====>

r = num %10   r = 0 %10 =1 
sum =sum + pow(r,digit)   # sum =153
num = num //10    num = 1 //10 = 0

if num ==sum :   ---->amg 
"""

"""n=int(input("enter the  number : "))  #1634 
digit = len(str(n))  # 4 
sum =0 
temp =n  # temp =1634
while n >0 :   # 0 > 0 
    r= n %10   # r =1 %10  = 1 
    sum =sum + pow(r,digit)  # sum = 1634 
    n = n //10    #  n =0
    
if temp ==sum :   #  0== 1634
    print("it is  amg number")
    
"""

# pelidrome  number  :
"""
n =121  ,141 ,131 ,11 ,22,33
output =121 ----> pelidrome number

"""
# twin number  : 

"""
n =123 

each digit  sum = 1+2+3 =6 
each digit multiple = 1*2*3 =6 

sum ==mul   ----> twin number
"""
n=int(input("enter the  number : "))  #123
sum =0 
mul =1 

while n >0 :  # 0 > 0 
    r= n %10    #   r = 1 %10 =1 
    sum =sum +r   # sum = 6 
    mul = mul *r  # mul =6
    n = n//10   # n =1 //10 =0
    
if sum ==mul :   # 6 == 6
    print("it is  twin number")

