#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:35:43 2018

@author: arpitansh
"""

'''
By using list comprehension, please write a program to print the list after
 removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

'''


lst = [12,24,35,70,88,120,155]
lst = [x for (i,x) in enumerate(li) if i%2!=0]
print (li)
