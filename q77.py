#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:28:49 2018

@author: arpitansh
"""

'''
Please write a program to print the list after removing delete even numbers
 in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

'''


lst = [5,6,77,45,22,12,24]
lst = [x for x in li if x%2!=0]
print (lst)