#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:56:43 2018

@author: arpitansh
"""
'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

'''

def fact(n):
    if n == 0:
        return 1
    else:
        return n* fact(n-1)
    
n = int(input('Enter the value of n ?  '))
print(fact(n))
    
    