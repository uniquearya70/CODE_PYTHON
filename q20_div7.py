#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:31:32 2018

@author: arpitansh
"""

class iterator(object):
	"""docstring for iterator"""
	def __init__(self, n):
		super(iterator, self).__init__()
		self.n = n
		
	def divBySeven(self):
		for i in range(0, self.n):
			if i % 7 == 0:
				yield i

lis = iterator(100).divBySeven()
for num in lis:
	print (num)



                
    
            
        
        