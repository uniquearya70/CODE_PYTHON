#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:14:11 2018

@author: arpitansh
"""

print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print (square(2))
print (square.__doc__)