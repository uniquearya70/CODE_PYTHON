#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:23:04 2018

@author: arpitansh
"""

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

inp = input('Enter input here: ')
dic = {'LETTERS':0, 'DIGITS':0}

for i in inp:
    
    if i.isdigit():
        dic['DIGITS']+=1
        
    elif i.isalpha():
        dic['LETTERS']+=1
        
    else:
        pass
    
print('LETTERS ',dic['LETTERS'])
print('DIGITS',dic['DIGITS'])