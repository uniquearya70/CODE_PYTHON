#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:08:41 2018

@author: arpitansh
"""

'''
Write a program to generate and print another tuple whose values are even numbers 
in the given tuple (1,2,3,4,5,6,7,8,9,10). 

'''

tp=(1,2,3,4,5,6,7,8,9,10)
lst=list()
for i in tp:
	if tp[i]%2==0:
		lst.append(tp[i])

tp2=tuple(lst)
print (tp2)