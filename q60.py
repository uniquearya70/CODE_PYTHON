#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:46:45 2018

@author: arpitansh
"""

'''
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be
 a console input.

'''

def fibo(n):
    if n==0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
n = int(input('Enter the value of n: '))
print(fibo(n))
    