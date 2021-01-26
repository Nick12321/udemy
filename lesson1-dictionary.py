#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:21:31 2021

@author: nick
"""

# continue from notebook

d_2 = {}
d_2['first'] = 100
print(d_2)

d_2['second'] = 200
print(d_2)

print(d_2['first'])

d_2['first'] = 110
print(d_2)

d_4 = {}
d1 = {'apple':10, 'pear':17}
d2 = {'potatoes':5, 'tomatoes':11}
d_4['d1'] = d1
d_4['d2'] = d2
print(d_4)

d1['apple'] +=1
print(d_4)

print(d1.get('apple'))
print(d1.get('banana'))
print(d1.get('banana', '"Banana not found"'))

##doesnt work because 'apple' is not directly accesible under d_4
#d_4.pop('apple')
#print(d1)

d1.pop('apple')
print(d1)
print(d_4)

#something weird happens here...the previous function changes d_4
#the follo0wing doesnt change d_4
d1 = {'apple':10, 'pear':17, 'pepper':283}
print(d_4)
print(d1)

d1.pop('pear')
print(d_4)

del d1['pepper']
print (d1)
print('\n')

#update function replaces and adds info from another dictionary
d_5 = {'apple':3, "pear":10}
print(d_5)
d_6 = {"apple":12, "banana":13}
d_5.update(d_6)
print(d_5)

print("banana" in d_5)

print(d_5.keys())
print(d_5.values())
print(d_5.items())

