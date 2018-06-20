#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:13:08 2018

@author: arpitansh
"""

'''
Please write a program to print the running time of execution of "1+1" for 100 times.



Hints:
Use timeit() function to measure the running time.

'''

from timeit import Timer
t = Timer("for i in range(100):1+1")
print (t.timeit())