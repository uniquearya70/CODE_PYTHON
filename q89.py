#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:23:22 2018

@author: arpitansh
"""

'''
Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.

'''

import itertools
print(list(itertools.permutations([1,2,3])))