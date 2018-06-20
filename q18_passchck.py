#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:13:33 2018

@author: arpitansh
"""

'''
A website requires the users to input username and password to register. Write 
a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

'''
import re
lst = []
inp = input('Enter password here: ').split(',')
item = [x for x in inp]
for p in item:
    if len(p)< 6 or len(p)>12:
        continue
    else:
        pass
    if not re.search('[a-z]',p):
        continue
    elif not re.search('[A-Z]',p):
        continue
    elif not re.search('[0-9]',p):
        continue
    elif not re.search('[$#@]',p):
        continue
    elif not re.search('[\s]',p):
        continue
    else:
        pass
    lst.append(p)
print(','.join(lst))
    
    
    
    
