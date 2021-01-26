# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:15:30 2021

@author: nick
"""

#variables and copies
dog = 1000
cat = dog
print(id(dog))
print(id(cat))
print(dog is cat)
print('\n')

cat = 123456
print(id(dog))
print(id(cat))
print(dog is cat)
print('\n')

#if, elif, and else
apple = 60
if apple > 50:
    print('OK')
print('\n')
   
banana = 30
if banana > 200:
    print('200')
elif banana <100:
    print('NOK')
else:
    print("OK 100-200")
print('\n')

list_1 = [123,456,789]
if 123 in list_1:
    print('ok')
print('\n')

dict_1 = {"apple":123, "pear":345}
if "apple" not in dict_1:
    print("NOK")
else:
    print('OK')
print('\n')

a=0
while a< 10:
    print(a)
    a += 1
print('\n')

b = {"welcome", "to", "Python"}
while b:
    c=b.pop()
    print(c)    

b = {"welcome", "to", "Python"}

