#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:40:29 2018

@author: arpitansh
"""

'''
Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].

'''
'''
li = [1,2,3,4,5,6,7,8,9,10]
evenNumber = filter(lambda x: x%2==0, li)
print(evenNumber)
'''

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print (evenNumbers)
