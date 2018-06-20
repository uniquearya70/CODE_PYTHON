#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:05:14 2018

@author: arpitansh
"""

'''
Define a class Person and its two child classes: Male and Female. All classes 
have a method "getGender" which can print "Male" for Male class and "Female" for
 Female class.

'''

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print (aMale.getGender())
print (aFemale.getGender())
