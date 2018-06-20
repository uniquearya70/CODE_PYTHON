#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 22:11:14 2018

@author: arpitansh
"""

'''
Define a function which can generate a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys. The function 
should just print the keys only.

'''
def printdict():
    d = dict()
    for i in range(1,21):
        d[i]=i**2
        
    for k in d.keys():
        print(k)
        
printdict()
