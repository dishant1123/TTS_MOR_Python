# tuple  :  immutable  -----> don't changes in tuple -----> ordered  

"""t1 =(12,35,67,89,45.78,"tisha")
print(t1)
print(type(t1))

t2 =23,46,56,356,234,"harshita","sujal",67j
print(t2)
print(type(t2))

t3=56,
print(type(t3))
"""

# built in function : len min max sorted sum 

"""t1=(12,45,67,-2,456,90,90.34)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1)) # asc to desc 
print(sorted(t1,reverse=True)) # desc to asc
print(sum(t1))   # 
"""

# slicing  : 

"""
t1=(12,45,67,-2,456,90,90.34)
# t1[4]=900   # update  not possible  in tuple  bcz of  tuple is immutable.
# print(t1)

print(t1[-5])   # r  ot  l 
print(t1[2:6])  # start  2  end index 6
print(t1[-2 : -6 :-1])  # start  -2  end index -6
print(t1[ : : -1])
"""
# method  : 
"""
t1=(12,45,67,-2,456,90,90.34)

print(t1.index(-2))
print(t1.index(90.34))

print(t1.count(45))
"""

# convert  : 

"""
task :1 
    input  t1=(12,45,67,-2,456,90,90.34)
    ouput  t1=(12,45,67,-2,456,90,90.34,"tisha")
"""
"""t1=(12,45,67,-2,456,90,90.34)

l1 = list(t1)
l1.append("tisha")
print(tuple(l1))
"""

# adv tuple : 

"""t1=((1,2,3),(4,5,6),(7,8,9))
#      0       1      2 
print(t1)
print(t1[0])
print(t1[0][-1])
print(t1[2][1:2])
"""

t2=([1,2,3],[4,5,6],[7,8,9])
#     0      1       2 

t2[2][2] =900 
print(t2) 

"""
A. error 
B. ([1,2,3],(4,5,6),[900,8,9])
c. none of the  above 
"""


