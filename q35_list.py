#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 22:20:07 2018

@author: arpitansh
"""

'''
Define a function which can generate and print a list where the values are square
of numbers between 1 and 20 (both included).

'''

def printList():
    
    lst =list()
    for i in range(1,21):
        #lst[i]=i**2
        
        lst.append(i**2)
    print(lst)
    
printList()


'''
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li)
		

printList()

'''