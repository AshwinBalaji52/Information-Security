# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:02:51 2021
@author: AshwinBalaji
"""
#import sys
import random
def findPoints():
    
    modulo = 13 #prime number
    pointList = [] 
    '''
    EQUATION == (y^2 = x^3 + x + 2) % modulo
    a = 1
    b = 6
    '''
    for x in range(0, modulo):
        point_x = (pow(x, 3) + x + 1) % modulo
        
        for y in range(0, modulo):
            point_y = pow(y, 2) % modulo
            
            if(point_x == point_y):
                pointList.append((x, y))
            else:
                continue
    e1 = random.choice(pointList)
    
    print("\nCurve Equation points : ",pointList)  
    print("Random point : ",e1)
      
    return e1
    
findPoints()