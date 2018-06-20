#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:57:32 2018

@author: arpitansh
"""

'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print 
this list after removing all duplicate values with original order reserved.


'''

def removeDuplicate( li ):
    newli=[]
    seen = set()         # store a number of values without duplicate.
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print (removeDuplicate(li))
