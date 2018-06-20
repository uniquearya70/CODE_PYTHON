#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:31:37 2018

@author: arpitansh
"""

'''
Write a program that accepts a sequence of whitespace separated words as input
 and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

inp = input('Type ur text here: ').split(' ')
word = ' '.join(sorted(list(set(inp))))
print(word)