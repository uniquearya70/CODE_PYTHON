#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:07:05 2018

@author: arpitansh
"""

'''
Write a program that accepts a sentence and calculate the number of upper case 
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''

inp = input('Enter input here: ')
dic = {'UPPER CASE':0,'LOWER CASE':0}
for c in inp:
    
    if c.isupper():
        dic['UPPER CASE']+=1
        
    elif c.islower():
        dic['LOWER CASE']+=1
        
        
    else:
        pass
    
print('UPPER CASE:', dic['UPPER CASE'])
print('LOWER CASE:',dic['LOWER CASE'])


