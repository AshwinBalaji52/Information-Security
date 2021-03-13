# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:38:19 2021

@author: dell
"""


# Python program for the extended Euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
    gcd, x, y = egcd(30, 50)
    print("The GCD is", gcd)
    print(f"x = {x}, y = {y}")