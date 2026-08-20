# nested loop  : 
"""
user range   -----> 200  - 1000   -----> prime   print  

syntax : 
for i in range(start ,end) :
    for j in range():
        logic : 

"""

# ex :1 ask user to enter the start  number and ending number print the prime number between two range. 

"""
start = int(input("enter the start number : "))
end = int(input("enter the end number : "))

for i in range(start,end+1) :   # 201 ,1001
    count =0    # count =0 
    for j in range(1,i+1) :   # 2,201     #  ----> 1,2,4,5,10,20,25,50,100,200
        if i % j ==0 :       # 200 % 2 ==0 
            count = count +1  # 8 
    if count ==2 :    # 8 ==2 
        print(i,end=" ")
        
"""

# ex :2 ask user to enter the start  number and ending number print the amg number between two range.

"""
1634 : 4 digit 

each power ==  =====> 1**4   6**4  3**4  4**4  -----> 1 +1296 + 81 +256  ----->1634 
"""
start = int(input("enter the start number : ")) # 153 
end = int(input("enter the end number : "))  # 10000 

for i in range(start,end+1) :   # 153 ,10000
    sum =0 
    digit = len(str(i)) # len(153)   ---->3 
    temp = i  # temp =153 
    
    while temp >0  :   # 0 > 0
        r= temp %10   # r = 1 %10 =1
        sum = sum + pow(r,digit)    # sum = 153
        temp = temp //10   # temp = 1 //10 =0  

    if sum ==i  :  # 153 ==153 
        print(i,end=" ")
        
# hw pelidrome number ,reverse number , perfect number  , twin number  :