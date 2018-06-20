#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 00:25:40 2018

@author: arpitansh
"""

'''
Write a program which accepts a string as input to print "Yes" if the string 
is "yes" or "YES" or "Yes", otherwise print "No". 

'''


inp = input('Enter input here: ')
if inp=='yes' or inp=='Yes' or inp=='YES':
    print ('Yes')
    
else:
    print('No')

'''
s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print ("Yes")
else:
    print ("No")
'''