#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 02:14:19 2018

@author: arpitansh
"""

'''
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

'''

s = input()
u = unicode( s ,"utf-8")
print (u)
