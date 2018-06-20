#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:56:45 2018

@author: arpitansh
"""
'''
You are required to write a program to sort the (name, age, height) tuples by 
ascending order where name is string, age and height are numbers. The tuples are 
input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.

'''
from operator import itemgetter, attrgetter 
l = []
while True:
    s = input('Enter name,age,score: ')
    if not s:
        break
    l.append(tuple(s.split(',')))
    
print(sorted(l,key=itemgetter(0,1,2)))