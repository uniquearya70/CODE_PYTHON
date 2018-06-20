#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:44:59 2018

@author: arpitansh
"""

lst = []
print('\nNo. which are divisible by 7 and not by 5 in the range of 2000-3200 are\n')
for i in range(2000,3200):
    if (i % 7 == 0) & (i % 5 != 0):
        lst.append(str(i))

print ('\t'.join(lst))
#print (lst)        