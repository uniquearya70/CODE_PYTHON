#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:59:54 2018

@author: arpitansh
"""

'''
Define a function which can print a dictionary where the keys are numbers between 
1 and 20 (both included) and the values are square of keys.

'''
'''
def dict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)
        
dict()
 '''
def printDict():
	d = dict()
	for i in range(1,21):
		d[i] = i**2
	print (d)
		

printDict()   
