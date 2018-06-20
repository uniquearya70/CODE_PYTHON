#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:38:36 2018

@author: arpitansh
"""

'''
By using list comprehension, please write a program generate a 3*5*8 3D array whose
 each element is 0.

'''


array_3d = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print (array_3d)