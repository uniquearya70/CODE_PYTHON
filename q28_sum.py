#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:52:20 2018

@author: arpitansh
"""

'''
Define a function that can receive two integral numbers in string form and compute
their sum and then print it in console.

'''

def SumFunction(n1,n2):
    return int(n1) + int(n2)

n1 = input('Enter n1:') 
n2 = input('Enter n2:')

print(SumFunction(n1,n2))


