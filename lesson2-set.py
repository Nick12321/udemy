#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:46:34 2021

@author: nick
"""

#lists contain duplicates, sets do not hold duplicates
list_1 = [222, 333, 444, 333]
list_1 = set(list_1)
print(list_1)
print('\n')

s_1= {1,2,3,4,4,5,5,6,6}
print(type(s_1))
print(s_1)