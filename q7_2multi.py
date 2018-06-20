#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 08:57:47 2018

@author: arpitansh
"""

'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional 
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
'''

inp = int(input('Give ur input here: ').split(','))
dimension = [i for i in inp]

rowNum = dimension[0]
colNum = dimension[1]

multilist = [[0 for col in range(colNum)] for row in range (rowNum)]


for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
        
print(multilist)
    

