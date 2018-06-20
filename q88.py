#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:19:43 2018

@author: arpitansh
"""

'''
Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

'''

s = input('Give ur input here: ')
s = s[::2]    # list[::2] to iterate a list by step 2.
print(s)