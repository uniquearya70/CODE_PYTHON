#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 23:54:28 2018

@author: arpitansh
"""

'''
Define a function which can generate a list where the values are square of numbers
 between 1 and 20 (both included). Then the function needs to print the last 5 
 elements in the list.

'''
def printlist():
    lst = list()
    for i in range(1,21):
        lst.append(i**2)
        
    print(lst[-5:])
    
printlist()
    