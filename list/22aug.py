# task  : 1 ask user to enter the  element  of  the  list  and append  to  another list  and separate the odd and even . 

"""n=int(input("enter the number of element in the list : "))
l1=[]
# 23 1 4 5 6    ----> l1= [23,1,4,5,6]  - ---> odd =[]   even =[] 
 
for i in range(n+1) :
    ele = int(input("enter the element : "))
    l1.append(ele)
    
print(l1)  # l1= [23,1,4,5,6]

odd =[] 
even =[] 

for i in l1:    # [23,1,4,5,6]
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i) 
print(odd)  # [1,5,6]
print(even)  # [23,4]
"""    

# task :2 
"""
take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]
"""

l1=[121 , 131 , 123 ,145 , 789 ,141]
l2=[] 

for i in l1:   # 121 ==121 
    if str(i) == str(i)[ : : -1] :  # "121"
        l2.append(int(i)) 
        
print(l2)




 
 