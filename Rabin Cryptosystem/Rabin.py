# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:56:33 2021

@author: Ashwin Balaji
"""
import sys
import math

def rabinEncryption(public_key, plainText):
    
    c = pow(plainText, 2) % public_key # n == Public Key
    return c

def rabinDecryption(prime_p, prime_q, c):
    
    a1 =  int(pow(c, (prime_p+1) / 4) % prime_p)
    a2 =  int(-pow(c, (prime_p+1) / 4) % prime_p)
    b1 =  int(pow(c, (prime_q+1) / 4) % prime_q)
    b2 =  int(-pow(c, (prime_q+1) / 4) % prime_q)
    #print(a1, a2, b1, b2)
    p1 = chineseReminder(a1, b1, prime_p, prime_q)
    p2 = chineseReminder(a1, b2, prime_p, prime_q)
    p3 = chineseReminder(a2, b1, prime_p, prime_q)
    p4 = chineseReminder(a2, b2, prime_p, prime_q)
    
    return p1, p2, p3, p4

def chineseReminder(a, b, p, q):
    m = p * q
    m1 = int(m/p)
    m2 = int(m/q)
    
    inv_m1 = extendedEuclidean(m1, p)
    inv_m2 = extendedEuclidean(m2, q)
    
    inv_m1 = inv_m1[1]
    inv_m2 = inv_m2[1]
    
    result = ((m1 * a * inv_m1) + (m2 * b * inv_m2)) % m
    
    return result

def checkPrime():
    flag = False
    flag1 = False   
    prime_p = int(input("Prime-Number (p) : "))
    prime_q = int(input("Prime-Number (q) : "))
    '''
    if (sympy.isprime(prime) == True):
        return prime
    else:
        print("Unexpected Input")
    '''
    if prime_p > 1:
        for itr in range(2, prime_p):
            if (prime_p % itr) == 0:
                flag = True
                break
    if prime_q > 1:
        for itr in range(2, prime_q):
            if (prime_q % itr) == 0:
                flag = True
                break 
            
    if flag == False and flag1 == False:
        k = extendedEuclidean(prime_p, 4)
        k = k[1] % 4
        k1 = extendedEuclidean(prime_q, 4)
        k1 = k1[1] % 4
        if (k == k1 == 3) or (k == k1 == 1):
            #print(k, k1)
            return prime_p, prime_q 
        else:
            sys.exit("Prime numbers are not in the form of (4K + 3) or (4K + 1)")
    else:
        sys.exit("Unexpected Input !!! Atleast one input is not prime ...") 

def extendedEuclidean(inverse, prime):
    if inverse == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % inverse, inverse)
        return gcd, y - math.floor(prime / inverse) * x, x 
    
def keyGeneration(prime_p, prime_q, n):
    public_key = n
    private_key = (prime_q, n)    
    return public_key, private_key   
    
def main():
    print("\n\t\t\tRABIN ASYMMETRIC CRYPTOGRAPHY")
    
    plainText = int(input("Plain-Text : "))
    
    prime_p, prime_q = checkPrime()
    
    public_key = prime_p * prime_q
    private_key = (prime_q, public_key) 
    print("\nPublic-Key : ",public_key)
    print("Private-Key : ",private_key)
    
    c = rabinEncryption(public_key, plainText) #n == PUBLIC KEY and c = CIPHER TEXT
    print("\nCipher-Text : ",c)
    
    p1, p2, p3, p4 = rabinDecryption(prime_p, prime_q, c)
    p1 = p1 % public_key
    p2 = p2 % public_key
    p3 = p3 % public_key
    p4 = p4 % public_key
    print("\nDecipher Text :",(p1, p2, p3, p4))
    
if __name__ == '__main__':
    main()
