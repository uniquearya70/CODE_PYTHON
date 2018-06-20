#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:32:16 2018

@author: arpitansh
"""

''' Q.With a given integral number n, write a program to generate a dictionary that
 contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
'''

n = int(input('Enter the value of n? '))
dic = dict()

for i in range(1,n+1):
    dic[i] = i*i
    
print(dic)


