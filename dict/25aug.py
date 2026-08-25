# dict :  mutable   -----> you change the  dict .  ---->store in  key value pair  
"""
in dict key  is  immutable  and  value  is  mutable.
"""

"""
d1={"phy" :90 ,"che" :99}   # phy  ----> key   90 value   che ---> key  99 value 
print(d1)
print(type(d1))
"""

"""
d2={89:90 , "maths" :78}
# 89  ----> key  90 value 
print(d2)
print(type(d2))
"""

# add in dict :

"""
d1={"phy" :90 ,"che" :99}   
d1['maths']=78 
print(d1)
"""
# update  the value  : 

"""
d1={"phy" :90 ,"che" :99}   

d1['phy'] =99 
print(d1)
"""

# built in function  : len min max sorted sum 
"""
d1={"phy" :90 ,"che" :99}   

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
print(sum(d1.values()))

"""

# method  : 

# d1={"phy" :90 ,"che" :99}   

# d2 =d1.copy()
"""d2=d1
d1['eng'] =45
print("d1=",d1)
print("d2 =",d2) 
"""

"""d1.clear()
print(d1)"""

"""print(d1.keys())
print(d1.values())
print(d1.items())
"""

# print(d1.get("che"))

# d1.pop("phy")
# d1.pop()  # error : its compulsory to give the key
# print(d1)

# print(d1.pop('phy'))

# fromkeys : 

# l1=["piyush","smit"]

#dict = 'piyush' : 50 , 'smit':50

"""d2=dict.fromkeys(l1,50)
print(d2)

d2['piyush']=90 
d2['smit'] =92
print(d2)
"""
# update : 

"""d1.update(d2)
print(d1)
"""


# task :1  
"""
1. Ask user to give name and marks of 5 different students. Store them in dictionary.

user = 3    --------> n 
name= piyush 
marks =40
name =smit
marks =80 
name =bhavesh
marks =89    -----> for loop  

output : d1={"piyush" :40 ,"smit" :80 ,"bhavesh" :89}
"""


