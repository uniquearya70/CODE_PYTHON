#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 01:30:34 2018

@author: arpitansh
"""

'''
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area. 
'''




class Rectangle(object):
    def __init__(self,l,w):
        self.length = l
        self.width = w
        
    def area(self):
        return self.length*self.width
    
arectangle = Rectangle(3,20.3)
print(arectangle.area())
