#set : mutable  -----> unordered -----> collection of unique element  ----> no  duplication  allow in the set

"""s1={23,56,78,45,23,45,90,"tisha",9j,"raj"}
print(s1)
print(type(s1))
"""

# empty set : 

"""s1=set()
print(s1)
print(type(s1))
"""
# note : set is  unordered collection of unique element so  we can't acacess though  the  index and slicing.

# built in function : len min max sorted sum 

"""
s1={23,45,67,89,23,45,12,90}
print(s1)
print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1))
print(sorted(s1,reverse=True))
"""

# method : 

# s1={23,45,67,89,23,45,12,90}

# s1.add(900)
# print(s1)

# s2=s1 
# s1[2] =90  # not  possible  bcz we can't access though  index in set  
# print(s1)

# s2=s1.copy()
# s1.add(400)
# print(s1)
# print(s2)


# s1.discard(232)  # if  element not present  in set  then  it  will  not  remove and print  original set
# print(s1)

# s1.remove(435) # if  element   not present  in set  then  it  will  give  keyerror
# print(s1)

# s1.pop()  # random element remove 
# print(s1)

"""s1={1,2,3,4,5}
s2={4,5,6,7}
s3={1,2,3,4,5,6,7,8,9,10}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1 -s2 
print(s2.difference(s1))  # s2 -s1

print(s1.symmetric_difference(s2))  #

""" 

# frozenset : it's  part of the set  -----> immutable ----> no duplication  allow in the frozenset -----> unordered


"""fz=frozenset([11,22,3,3,5,6,7,8,9,11])
print(fz)
print(type(fz))

"""