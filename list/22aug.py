# task  : 1 ask user to enter the  element  of  the  list  and append  to  another list  and separate the odd and even . 

n=int(input("enter the number of element in the list : "))
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
    


 
 