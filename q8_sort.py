#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:56:19 2018

@author: arpitansh
"""

inp = [x for x in input('Enter string here: ').split(',')]
inp.sort()
#print(inp)
print(','.join(inp))