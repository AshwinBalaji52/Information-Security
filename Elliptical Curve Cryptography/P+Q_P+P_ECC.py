# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:20:30 2021

@author: dell
"""
import math
from fractions import Fraction 
count = 2
def addPoints():
    e1 = (2, 0)
    x = temp_x = e1[0]
    y = temp_y = e1[1]
    d = int(input("Enter d : "))
    #d = 
    #a = 2
    #b = 3
    temp_e = addsamePoint(x, y, x, y)
    temp_x = temp_e[0]
    temp_y = temp_e[1]
    
    for add in range(0, d-2):
        if(e1 == temp_e):
            temp_x, temp_y = addsamePoint(temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
            
        else:
            temp_x, temp_y = adddifferentPoint(temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
    e2 = temp_e
    print("\ne2 :", e2)
    return

def addsamePoint(x1, y1, x2, y2):
    lambda_eq = Fraction((3 * pow(x1, 2) + 2) , (2 * y1)) #Fraction(a / b)
    #print("\n")
    '''
    a = (x1, y1)
    b = (x2, y2)
    print(a == b)
    '''
    print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    print("Lambda : ",lambda_eq)
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator, 13)
    print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1])
    
    x = (pow(lambda_cal,2) - x1 - x2) % 13
    print("X : ",x)
    y = (lambda_cal * (x1 - x) - y1) % 13
    print("Y : ",y)
    
    return x, y

def adddifferentPoint(x1, y1, x2, y2):
    lambda_eq = Fraction((y2 - y1), (x2 - x1))#Fraction(a / b)
    print("\n")
    '''
    to check whether both the tuples are correct or not
    a = (x1, y1)
    b = (x2, y2)
    print(a == b)
    '''
    print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    print("Lambda : ",lambda_eq)
    
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator,13)
    print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1])
    #print(lambda_cal)
    
    x = (pow(lambda_cal,2)- x1 - x2) % 13
    print("X : ",x)
    
    y = (lambda_cal * (x1 - x) - y1) %13
    print("Y : ",y)
    
    #print(Fraction(x % 67,y % 67))
    return x, y

def extendedEuclidean(denominator, prime):
    if denominator == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % denominator, denominator)
        return gcd, y - math.floor(prime / denominator) * x, x #gcd, y - (prime // denominator) * x, x

#addPoints(10,1,10,1)
addsamePoint(8,1,8,1)
adddifferentPoint(7,5,8,1)