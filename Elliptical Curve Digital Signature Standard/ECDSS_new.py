# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:11:38 2021
@author: AshwinBalaji
"""

import sys
import random
import math
from fractions import Fraction 
import matplotlib.pyplot as plt
import hashlib

def checkPrime(prime):
    flag = False
    if prime > 1:
        for itr in range(2, prime):
            if (prime % itr) == 0:
                flag = True
                break
    if flag == True:
        sys.exit("Error ... Expected value is not a prime number !!! ") 
    else:
        return prime
    
def findPoints(prime, a, b):
    pointList = [] 
    for x in range(0, prime):
        point_x = (pow(x, 3) + a * x + b) % prime
        
        for y in range(0, prime):
            point_y = pow(y, 2) % prime
            
            if(point_x == point_y):
                pointList.append((x, y))
            else:
                continue
    '''
    remove(a,0) type of element(s) as it may give fraction a/0 issue
    '''
    for x in pointList:
        if(x[1] == 0):
            pointList.remove(x)
    #print("Curve equation points GF[Prime_P]: ", pointList)       
    e1 = random.choice(pointList)
    return e1   

def addPoints(a, prime, randomInt, e1):
    x = temp_x = e1[0]
    y = temp_y = e1[1]
    
    temp_e = samePoint(a, prime, x, y, x, y)
    temp_x = temp_e[0]
    temp_y = temp_e[1]
    
    for add in range(0, randomInt-2):
        if(e1 == temp_e):
            temp_x, temp_y = samePoint(a, prime, temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
            
        else:
            temp_x, temp_y = differentPoint(prime, temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
    e2 = temp_e
    
    return e2

def samePoint(a, prime, x1, y1, x2, y2):
    if y1 == 0:
        sys.exit("Error !!! Denominator is 0")
    lambda_eq = Fraction((3 * pow(x1, 2) + a) , (2 * y1)) #Fraction(a / b)
    #print("\n")
    #print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    #print("Lambda : ",lambda_eq)
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator, prime)
    #print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1]) % prime
    
    x = (pow(lambda_cal,2) - x1 - x2) % prime
    #print("X : ",x)
    y = (lambda_cal * (x1 - x) - y1) % prime
    #print("Y : ",y)
    
    return x, y

def differentPoint(prime, x1, y1, x2, y2):
    if x2 == x1:
        sys.exit("Error !!! Denominator is 0")
    lambda_eq = Fraction((y2 - y1), (x2 - x1))#Fraction(a / b)
    #print("\n")
    #print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    #print("Lambda : ",lambda_eq)
    
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator, prime)
    #print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1]) % prime
    #print(lambda_cal)
    x = (pow(lambda_cal,2)- x1 - x2) % prime
    #print("X : ",x)
    
    y = (lambda_cal * (x1 - x) - y1) % prime
    #print("Y : ",y)
    return x, y

def extendedEuclidean(denominator, prime):
    if denominator == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % denominator, denominator)
        
        return gcd, y - (prime // denominator) * x, x #or gcd, y - (prime // denominator) * x, x

def signing(a, d, r, e1, prime_p, prime_q, plainText):
    result_P = addPoints(a, prime_p, r, e1) #P(u, v) & u%q = s1
    print("\nP(U, V):", result_P)
    s1 = result_P[0] % prime_q
    #print("S1 : ", s1)
    inverse_r = extendedEuclidean(r, prime_q)[1] % prime_q #in tuple 1st position is the actual inverse value
    #print(inverse_r)
    #print(hash(plainText))
    hashed = hashing(plainText) % prime_q
    #print("hashed s :", hashed)
    #print(hashed % prime)
    s2 = ((hashed + d * s1) * inverse_r) % prime_q
    #print(s2)
    return s1, s2
    
def verifying(signature1, signature2, plainText, public_key):
    inverse_s2 = (extendedEuclidean(signature2, public_key[3])[1]) % public_key[3]#public_key[3] = prime_q
    #print(inverse_s2)
    hashed = hashing(plainText) % public_key[3]
    #print("hashed v :", hashed)
    interim_A = (hashed * inverse_s2) % public_key[3]
    interim_B = (inverse_s2 * signature1) % public_key[3]
    print("interim A B:", (interim_A, interim_B))
    temp_A = addPoints(public_key[0], public_key[3], interim_A, public_key[4])
    temp_B = addPoints(public_key[0], public_key[3], interim_B, public_key[5])
    #print(temp_A == temp_B)
    if temp_A == temp_B:
        temp_T = samePoint(public_key[0], public_key[3], temp_A[0], temp_A[1], 
                           temp_B[0], temp_B[1])
    else:
        temp_T = differentPoint(public_key[3], temp_A[0], temp_A[1], 
                           temp_B[0], temp_B[1])        
    print("\nT(X, Y) :", temp_T)
    verify = temp_T[0] % public_key[3] #T(x, y) -> x mod prime_q
    return verify

def hashing(plainText):
    h = hashlib.sha256(plainText.encode('utf-8')).hexdigest()
    n = int(h, base = 16)
    return n

def main():
    print("\n\t\t\tELLIPTICAL-CURVE DIGITAL SIGNATURE STANDARD")
    
    plainText = input("Plain-Text : ")
    
    a, b = input("Coefficients a & b : ").split()
    print("\nCurve Equation: y^2 = x^3 +",a,"x +",b)
    a = int(a)
    b = int(b)
    
    p, q = input("Prime Numbers p & q : ").split()
    prime_p = checkPrime(int(p))
    prime_q = checkPrime(int(q))
    
    #e1 = findPoints(prime_p, a, b)
    #e1 = (49, 22)
    e1 = (3, 16)
    print("\nRandom-point on the curve (e1): ",e1)
    
    d = int(input("Sender's Private-Key (d) : "))
    
    e2 = addPoints(a, prime_p, d, e1)
    print("\nSecond point (e2) on the curve by solving (d * e1) :", e2)
    
    r = int(input("Random-Secret (r) : "))
    
    public_key = (a, b, prime_p, prime_q, e1, e2)
    print("\nSender's Public-Key :", public_key)
    
    signature1, signature2 = signing(a, d, r, e1, prime_p, prime_q, plainText)
    print("\nSignature (S1, S2):", (signature1, signature2))
    
    verify = verifying(signature1, signature2, plainText, public_key)
    
    if verify ==  signature1:
        print("\nSecured [Signature 1 == Verify]")
    else:
        print("\nBreached  [Signature 1 != Verify]")
    
if __name__ == '__main__':
    main()