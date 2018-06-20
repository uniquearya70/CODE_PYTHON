#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:27:54 2018

@author: arpitansh
"""

'''
Please write a program using generator to print the even numbers between 0 and n
 in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

'''

def even(n):
    i = 0
    while i<n:
       if i%2==0:
           yield i
       i = i+1
       
n = int(input('Value: '))
values = []
for i in even(n):
    values.append(str(i))
    
print(','.join(values))
    
        