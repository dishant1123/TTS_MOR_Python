"""
file handling  :  txt file  

1. read    : exiting file  open  ----> only  read 
2. write   : new file  create + write  ----> exiting file  open  ----> overwrite 
3. append  : new file  create + write  ----> exiting file  open  ----> last add 

fopen ----> file  open  , with open  
fclose  ---> file close 


"""
# ex :1  w mode  : 

"""
with open("varun.txt",'w') as f :
    f.write("my name is varun.\n")
    f.write("my age is 21.\n")
    f.write("my hobby is palying cricket.\n")
    f.write("dream to meet virat kohli.\n")
    
    f.close()
"""

# ex :2 w mode exiting  open  : 
"""
with  open("bhavesh.txt",'w') as f :
    f.write("best friend name is  varun.\n")
    f.write("live  in ahmedabad.\n")
    f.write("dream to meet narendra modi.\n")
    f.close()
"""

#ex :3 append mode 

"""
with open("vishnu.txt",'a') as f :
    f.write("my name is vishnu.\n")
    f.write("my age is 21.\n")
    f.write("my hobby is palying football.\n")
    f.write("dream to meet messi.\n")
    
    f.close()
"""

# ex: 4 append mode exiting  open  :
"""with open("vishnu.txt",'a') as f :
    f.write("best friend name is  ganpat.\n")
    f.write("live  in ahmedabad.\n")
    f.close()
"""

# ex : 5 read mode :

"""
with  open("vishnu.txt",'r') as f :
    # c=f.read()
    # c=f.readline()
    c=f.readlines()
    print(c)
    f.close() 
"""
# exception handling : 

"""
syntax : 

try : 
    code 
exception 
    code 
finally :
    print()

"""

# ex :1 

"""try :
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print("div of two number is  : ",a/b)
except ZeroDivisionError :
    print("you can't divide by zero")
"""

# ex :2 
"""try :
    l1=[12,45,67,89,23,56]
    print(l1[2])
except IndexError :
    print("index out of range")
    
finally :
    print("end of program")
"""

# ex :3 filenotfound error : 
"""
try : 
    with  open("vishnu.txt",'r') as f :
        c=f.read()
        print(c)
        f.close()
except FileNotFoundError :
    print("file nahi mil rahi he  toopaa")

finally :
    print("aavjo  byebbye")
"""    
    
# generator  function  : 

# ex :1 

"""def gen():
    yield 1
    yield 2
    yield 3
    
g=gen()
print(next(g))
print(next(g))
print(next(g))
"""

# ex :2 

"""def fruits():
    l1 = ["apple","banana","cherry","kiwi"]
    for i in l1 :
        yield i
f=fruits()
print(next(f))  
print(next(f))  
print(next(f))  
print(next(f))  
"""

# ex :3 enumerate  :
"""l1 = ["apple","banana","cherry","kiwi"]

for i in enumerate(l1) :
    print(i)
"""
"""
0  apple
1  banana
2  cherry
3  kiwi
"""

# ex : 4 zip 
"""
l1=["apple","banana","cherry","kiwi"]
country =["jammu","kerala","delhi","mumbai"]

for i in zip(l1,country) :
    print(i)
"""

# tasks :
"""
1. ask user to enter the string and  seperate  the  vowel  and  consonant in two different file that is  vowel.txt  and  consonant.txt

input :  my name is varun. 

vowel.txt : aeiau 
consonant.txt : my nm s vrn.

"""

