#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:39:07 2018

@author: arpitansh
"""

'''
Please write a program which accepts basic mathematic expression from console
 and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.

'''

expression = input('Enter ur expression here: ')
print(eval(expression))