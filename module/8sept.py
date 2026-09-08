# python  in  built  module  : 
"""
random , math ,datetime,time ,cal
"""

import random as r 

"""
print(r.random())  #ranoom number  generate  between  0  and  1 ---> exclude
print(r.randrange(1,20,2))  #  last number exclude
print(r.randint(1,10))  # both number include
print(r.choice([1,2,3,4,5,"ganpat","vishnu"]))  # random choice
print(r.choices([1,2,3,"ganpat","vishnu"],k=3))  # random choices

r.seed(45)  # number  fix 
print(r.randint(1,10))
"""

import math as m

"""print(m.factorial(5))
print(m.sqrt(25))
print(m.pi)
print(m.e)
print(m.pow(2,3))
print(m.floor(3.45))  # int  value  only 
print(m.ceil(3.01))  # round up
print(m.fsum([1,2,3,4,5]))
"""

# data time  : 

import datetime as dt

# today = dt.datetime.today()
# today = dt.datetime.today().strftime("%d-%m-%Y %H:%M:%S %p %A  %b")
# print(today)

# now =dt.datetime.now()
# print(now)

"""date = dt.datetime(2026,9,8,8,42,12)
print(date)
print(date.month)
print(date.day)
print(date.year)
print(date.hour)
print(date.minute)
print(date.second)
"""

import time as t 

"""
now = t.time()
print(now)  # EPOCH time 

st =t.localtime()
print(st)

for i in range(1,10):
    print(i)
    t.sleep(0.50)
"""    

# game  :  using  random module  
"""
1.rock  2.paper  3.scissor

1. random.choice ["rock","paper","scissor"]
2. for  loop (10)
3. user score =0 computer score =0

4. condition  : 
        if (u ==r and  c==r) or ( u==s and c==s) or(u==p and c==p) :
            print("tie")
        elif () : 
            print("user win")
            user_score +=1 
        else :
            print("computer win")
            computer_score +=1
            
    case 1 : user win  : 
    u==r c==s ----> user win 
    u==p c==r ----> user win 
    u==s c==p ----> user win
    
5. score compare : 
    if userscore > computerscore :
        print("user win")
    else :
        print("computer win")

"""


