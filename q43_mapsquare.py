#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:47:40 2018

@author: arpitansh
"""

'''
Write a program which can map() to make a list whose elements are square of 
elements in [1,2,3,4,5,6,7,8,9,10].

'''



li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print (squaredNumbers)

'''
lst = [1,2,3,4,5,6,7,8,9,10]
squarelst = map(lambda x: x**2, lst)
print(squarelst)
'''