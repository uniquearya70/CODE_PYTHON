#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 01:18:10 2018

@author: arpitansh
"""

'''
Define a class named American which has a static method called printNationality.

'''

class American(object):
    @staticmethod
    def printNationality():
        print ('America')

anAmerican = American()
anAmerican.printNationality()
American.printNationality()