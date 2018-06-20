#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:51:03 2018

@author: arpitansh
"""

'''
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program
to make a list whose elements are intersection of the above given lists.

'''

set1 = set([1,3,6,78,35,55])
set2 = set([12,24,35,24,88,120,155])

set1 &= set2   #Intersection of set
lst = list(set1)
print(lst)