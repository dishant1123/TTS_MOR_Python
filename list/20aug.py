"""
python  data type  : 

1. string  : immutable  -----> you can't change the string
2. list  : mutable  -----> you can change the list ---->ordered collection
3. tuple  : immutable  -----> you can't change the tuple
4. dictionary  : mutable  -----> you can change the dictionary  ----> key value pair
5. set  : mutable  -----> you can change the set ---> no duplicate value ----> unordered collection

"""

# list  :  mutable  ordered collection ---->change the list
"""
l1=[12,34,56,78,90,34.67,True,78j,"yug",12]

print(l1)
print(type(l1))
"""
# slice  :
"""
access index number   :  ----> index number start from 0 

"""
"""l1 =[12,34,56,78,90,34.67,122]
 #    0 1  2  3  4  5     6 
# positive index number  :   -----> direction  ----> l  to  r 
# negative index number  :   -----> direction  ----> r  to  l

print(l1[0])  # 0 index  ----> element 
print(l1[4])
print(l1[6])
print(l1[-1])
print(l1[-5])
print(l1[ 2:5])  # start  2  end index 5  -----> end  excluded 
print(l1[ : 5])
print(l1[0 : ])
print(l1[ 2 : 6 :2 ])  # start index 2  end index 6  step  2 
print(l1[ 0 : 5 :3 ])  # start index 0  end index 5  step  3 
print(l1[  :  :2 ])  #
print(l1[  :  :-2 ])  #
print(l1[  :  :-1 ])  #reverse list 
"""

# built in function  :  len min max sort sum 
"""
l1 =[12,34,56,78,90,34.67,122]

print(len(l1))  # length of list
print(min(l1))  # minimum value of list
print(max(l1))  # maximum value of list
print(sorted(l1))  # sorted list
print(sum(l1))  # sum of list

"""

# method : 

"""l1 =[12,34,56,78,90,34.67,122,12]


l1.append(233)  # last  add 
print(l1)

l2 = l1.copy()
print(l2)

l1.clear()
print(l1)

l1[2] =900  # -----> update 
print(l1)

l2 =['apple','banana','cherry','date','fig','grape','kiwi']

l1.extend(l2)
print(l1)

print(l1.index(122))
print(l1.index(12))
print(l1.index(12,1,20))  # start index 1  end index 20

print(l1.count(12))  # count the number of 122

l1.sort()
print(l1)

print(l1.reverse())

l1.insert(3,800)   # index , element 
print(l1)

l1.pop()   # if no  arg  ----> last element  remove 
l1.pop(2)     # if arg  then remove  index number wise 
print(l1)

l1.remove(122)  # specify the element to remove
print(l1)
"""
"""
pop  : index wise remove element   ----> its not compulsory to enter the arg. 
remove  : arg is  compulsory  and  specify the element to remove

"""
