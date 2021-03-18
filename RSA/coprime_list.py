# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:33:06 2021

@author: Ashwin Balaji
"""
'''
Common factors of two number must be 1 i.e., GCD(A,B) == 1
it's kind of z*n (n can be odd or even)
In this relatively prime is also included if we delete 1 from list
'''
import math
def extendedEuclidean(inverse, n):
    if inverse == 0:
        return n, 0, 1
    else:
        gcd, x, y = extendedEuclidean(n % inverse, inverse)
        return gcd, y - math.floor(n / inverse) * x, x 

def coPrime(n):
    
    number_list = []
    coprime_list = []
    
    for number in range(1, n):
        number_list.append(number)
   
    for coprime in number_list:
        gcd  = extendedEuclidean(coprime, n)
        if (gcd[0] == 1):
            coprime_list.append(coprime)
            number_list.remove(coprime)
        else:
            number_list.remove(coprime)
            
    print(coprime_list)
        
coPrime(7)