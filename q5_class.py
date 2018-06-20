#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:56:53 2018

@author: arpitansh
"""

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class InputOutputString():
    
    def __init__(self):
        self.s = ""
        
    def getString(self):
        print('Enter the input string: ')
        self.s = input()
        
    def printString(self):
        print('Input string is:',self.s)
        
strObj = InputOutputString()
strObj.getString()
strObj.printString()

    