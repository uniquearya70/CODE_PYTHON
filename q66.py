#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:50:34 2018

@author: arpitansh
"""

'''
Please write a binary search function which searches an item in a sorted list.
 The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
'''
'''

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)
'''

import math
def bin_search(lst,element):
    bottom = 0
    top = len(lst)-1
    index = -1
    while top>=bottom and index ==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if lst[mid] == element:
            index = mid
        elif lst[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
            
    return index
lst = [2,5,7,9,11,11,17,33]
print(bin_search(lst,11))
print(bin_search(lst,42))