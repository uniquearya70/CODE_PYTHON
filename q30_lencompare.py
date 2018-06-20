#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:16:59 2018

@author: arpitansh
"""

'''
Define a function that can accept two strings as input and print the string 
with maximum length in console. If two strings have the same length, then the 
function should print all strings line by line.

'''

def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print (s1)
	elif len2>len1:
		print (s2)
	else:
		print (s1)
		print (s2)
        
#s1 = input('Enter ur first string here: ')
#s2 = input('Enter ur first string here: ')
		

printValue("Radio","Wallapvt")
