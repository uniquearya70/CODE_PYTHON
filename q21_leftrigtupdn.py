#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 13:57:52 2018

@author: arpitansh
"""

'''
A robot moves in a plane starting from the original point (0,0). The robot can 
move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot 
movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the 
distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
'''

import math
pos = [0,0]
print('Give directions and input here: ')
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))