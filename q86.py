#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:08:53 2018

@author: arpitansh
"""

'''
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

'''


dicti = {}
s=input('Enter string here: ')
for s in s:
    dicti[s] = dicti.get(s,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dicti.items()]))
