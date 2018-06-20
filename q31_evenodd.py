#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:37:19 2018

@author: arpitansh
"""

'''
Define a function that can accept an integer number as input and print the "It is
 an even number" if the number is even, otherwise print "It is an odd number".
 
'''
 
def evenOdd(n):
    if n%2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

n = int(input('Enter the value: '))   
print(evenOdd(n))
 