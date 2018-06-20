#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:50:09 2018

@author: arpitansh
"""

'''
Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

num = input('enter the list of number: ')

lst = num.split(',')
tple = tuple(lst)

print(lst)
print(tple)
 

