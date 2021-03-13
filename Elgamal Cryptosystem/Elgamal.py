# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 01:24:55 2021

@author: AshwinBalaji
"""
#import sympy
import random
import sys
import math

def elgamalEncryption(e1, e2, prime, plainText):
    
    zpGroup = []
    for group in range(1, prime):
        zpGroup.append(group)
        
    r =  random.choice(zpGroup)
    
    print("Random integer from the Z*p group : ", r)
    c1 = pow(e1, r) % prime
    c2 = (plainText * pow(e2, r)) % prime
    print("\nCipher Text : ", (c1, c2))

    return c1, c2

def elgamalDecryption(d, prime, c1, c2):
    calculateInverse = extendedEuclidean(pow(c1, d), prime)
    return (c2 * calculateInverse[1]) % prime

def extendedEuclidean(c1_inverse, prime):
    if c1_inverse == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % c1_inverse, c1_inverse)
        return gcd, y - math.floor(prime / c1_inverse) * x, x  
    
def checkPrime():
    
    flag = False
    prime = int(input("Prime Number : "))
    '''
    
    if (sympy.isprime(prime) == True):
        return prime
    else:
        print("Unexpected Input")
    '''
    if prime > 1:
        for itr in range(2, prime):
            if (prime % itr) == 0:
                flag = True
                break
    if flag == True:
        sys.exit("Unexpected Input") 
    else:
        return prime

def primitiveRoot(prime):
    
    zpGroup = []
    relatively_primelist = []
    primitive_root = []
    e1 = 0
    
    for relativelyPrime in range(1, prime):
        zpGroup.append(relativelyPrime)
   
    for relativelyPrime in zpGroup:
        for relativelyPrime1 in zpGroup:  
            relatively_primelist.append(pow(relativelyPrime, relativelyPrime1) % prime)
        relatively_primelist.sort()
        
        if relatively_primelist == zpGroup:
            primitive_root.append(relativelyPrime)
            relatively_primelist.clear()
        else:
            relatively_primelist.clear()
            continue
    
    e1 = random.choice(primitive_root)
    return e1

def privateKey(e1, prime):
    keyList = []
    for keys in range(1, prime-2+1): #range works till n-1
        keyList.append(keys)
    
    d = random.choice(keyList)
    return d
    
def keyGeneration():
    
    prime =  checkPrime()
    e1 = primitiveRoot(prime)
    d = privateKey(e1, prime)
    e2 = pow(e1, d) % prime
    public_key = (e1, e2, prime)
    private_key = d
    print("Public Key : ", public_key)
    print("Private Key : ", private_key)

    return e1, e2, prime, d #e1, e2, prime is public key and d is private key

def main():
    print("\n\t\t\tELGAMAL ASYMMETRIC CRYPTOGRAPHY")
    plainText = int(input("Plain-Text : "))
    e1, e2, prime, d = keyGeneration()
    c1, c2 = elgamalEncryption(e1, e2, prime, plainText)
    decryptedText = elgamalDecryption(d, prime, c1, c2)
    print("\nDecipher Text :", decryptedText)
    
if __name__ == '__main__':
    main()
