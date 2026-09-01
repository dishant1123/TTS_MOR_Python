# string : immutable  ---> you can't change the string ----> collection of  character

"""
s1="my name is tisha nagrani."
print(s1)
print(type(s1))
"""

# built in function : len min max sorted sum
"""
s1="my name is tisha nagrani."

print(s1)
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))

"""
# slicing : 

"""s1="my name is tisha nagrani."
#   0123 ....................
# index -----> start 0     -----> l to r 
# neg index : start -1   -----> r ot  l 

print(s1[2])
print(s1[2:5])
print(s1[-2 :])
print(s1[1 : 10 :2])
print(s1[  :  :3])
print(s1[  :  :-2])
print(s1[  :  :-1])
"""


# task :1  using  slicing  only
"""
input  : dishant dipakkumar shah 
output : d.d.shah

"""

# task :2 ask user to enter the two  string and  interchange the  first  three character and  vice versa .  using slicing only 
"""
input  a: color 
input  b: full 

output a: fulor 
output b: coll

"""
s1=input("enter the  string  1: ")   # color 
s2=input("enter the  string  2: ")   # full 
 

result = s2[0 :3] + s1[3: ]
result2 = s1[0 :3]+ s2[3:]
print("output a:",result)
print("output b:",result2)