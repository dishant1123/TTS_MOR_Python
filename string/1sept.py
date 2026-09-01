# method  : 

s1="My name is piyush sahenani."

# case related method : 
"""print(s1.capitalize())  # first letter capital 
print(s1.lower())       # all letter small
print(s1.upper())       # all letter capital
print(s1.title())       # first letter capital and rest small
print(s1.swapcase())
print(s1.casefold())
"""

# count :
"""print(s1.count("is"))
print(s1.count("i"))
print(s1.count("i",8,20))
"""

# index , rindex , find , rfind : 

s1="My name is piyush sahenani."

"""print(s1.index("i"))  #8
print(s1.index("is"))  # 8
print(s1.index("piyush"))
print(s1.find("i"))  #8
print(s1.find("is"))  # 8
print(s1.find("piyush")) 
"""
# hw : diff between  index , find  and  rindex rfind 

"""print(s1.rindex("i"))  
print(s1.rindex("s"))  
print(s1.rindex("sh"))
print(s1.rfind("i"))  
print(s1.rfind("s"))
print(s1.rfind("sh"))
print(s1.index('i',9,20))
"""
# split ,rsplit ,partition , rpartition :

s1="My name is piyush sahenani."

"""print(s1.split())
print(s1.split("i"))
print(s1.rsplit("s"))

print(s1.partition("i"))  # divide string into 3 parts
print(s1.partition("is")) 
print(s1.partition("My name")) 

print(s1.rpartition('i'))
print(s1.rpartition('s'))
"""

# replace , strip , rstrip , lstrip : 

"""s2="               hello ganpat         "
print(s2)
print(s2.strip())  # remove the leading and trailing whitespaces
print(s2.lstrip()) # remove the leading whitespaces left side
print(s2.rstrip()) # remove the leading whitespaces right side

s3="the  lion in the  cage."
print(s3.replace("the",""))
print(s3.replace("the","",1))
print(s3.replace("the","",2))
print(s3.replace("the","a",1))
"""

# join  : 

"""l1 =["hello","roshani","tisha"]
# hello roshani tisha
result =" ".join(l1)
print(result)
"""

# isalpha , isdigit ,isalnum : 

"""s4="roshanisigh"
print(s4.isalpha()) # check  the  string  contains  alphabet

s5="smitthakker3107"
print(s5.isalnum()) # check  the  string  contains  alphabet and number

s6="1211"
print(s6.isdigit()) # check  the  string  contains  number 0 -9 
"""


