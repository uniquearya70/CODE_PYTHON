#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 01:22:08 2018

@author: arpitansh
"""

'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

'''

class Circle(object):
    def __init__(self,r):
        self.radius = r
        
    def area(self):
        return self.radius**2*3.14
    
acircle = Circle(5)
print(acircle.area())