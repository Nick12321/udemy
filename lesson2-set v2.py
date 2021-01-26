# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:58:37 2021

@author: nick
"""

list_1 = [222,333,444,333]
print(list_1)
list_1 = set(list_1)
print(list_1)
print('\n')

s_1 = {1,2,3,4,4,5,6,6,7}
print(type(s_1))
print(s_1)
print('\n')

a = {1,2,3,4,5}
b = {2,3,4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print('\n')

print(a.difference(b))
print(b.difference(a))
print(a - b)
print(b - a)
print('\n')

c = {1,2,3,4,5}
d = {1,2,3}
print(d.issubset(c))
print(c.issubset(d))
#same as
print(d<=c)
print(d > c)
print('\n')

#add numbers to list
e = {1,2,3,4}
e.add(5)
print(e)
e.update([5,6,7])
print(e)
e.remove(1)
print(e)
e.pop()
print(e)