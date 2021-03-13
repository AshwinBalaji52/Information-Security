# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:46:32 2021

@author: dell
"""


def primitiveRoot(prime):
    
    zpGroup = []
    relatively_primelist = []
    primitive_root = []
    e1 = 0
    
    for relativelyPrime in range(1, prime):
        zpGroup.append(relativelyPrime)
    #print(zpGroup)
   
    for relativelyPrime in zpGroup:
        for relativelyPrime1 in zpGroup:  
            relatively_primelist.append(pow(relativelyPrime, relativelyPrime1) % prime)
        relatively_primelist.sort()
        
        if relatively_primelist == zpGroup:
            primitive_root.append(relativelyPrime)
            #print(primitive_root)
            relatively_primelist.clear()
        else:
            relatively_primelist.clear()
            continue
    print(primitive_root)
        
primitiveRoot(11)