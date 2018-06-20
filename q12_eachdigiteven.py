#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:01:49 2018

@author: arpitansh
"""

'''
Write a program, which will find all such numbers between 1000 and 3000 
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a 
single line.
'''

rslt = []
for i in range (1000,3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        rslt.append(s)
        
print(','.join(rslt))
        
    
    
