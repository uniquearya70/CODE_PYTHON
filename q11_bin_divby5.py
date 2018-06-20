#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:45:09 2018

@author: arpitansh
"""
'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. The numbers 
that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

'''


rslt = []
inp = input('Enter ur input here: ').split(',')
item = [x for x in inp]

for p in item:
    intp = int(p,2)     #convert binary to decimal
    if intp % 5 == 0:
        rslt.append(p)
        
print(rslt)