#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:38:26 2018

@author: arpitansh
"""

'''
Write a program that computes the net amount of a bank account based a transaction
 log from console input. The transaction log format is shown as following:
D 100
W 200

'''

netAmount = 0
while True:
    s = input('Enter the transaction: ')
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print ('Net amnt', netAmount)