# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:19:17 2021

@author: Ashwin Balaji
"""
import sys
import random
import math

def checkPrime():
    flag = False
    flag1 = False   
    prime_p = int(input("Prime-Number (p) : "))
    prime_q = int(input("Prime-Number (q) : "))

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
            return prime_p, prime_q 
    else:
        sys.exit("Unexpected Input !!! Atleast one input is not prime ...")

def extendedEuclidean(inverse, n):
    if inverse == 0:
        return n, 0, 1
    else:
        gcd, x, y = extendedEuclidean(n % inverse, inverse)
        return gcd, y - math.floor(n / inverse) * x, x #gcd, y - (n // inverse) * x, x 

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
    e  = random.choice(coprime_list)

    return e
    
def rsaEncryption(plainText, e, n):
    
    cipherText = pow(plainText, e) % n
    
    return cipherText

def rsaDecryption(cipherText, d, n):
    
    decipherText = pow(cipherText, d) % n
    
    return decipherText

def main():
    print("\n\t\t\tRSA ASYMMETRIC CRYPTOGRAPHY")
    plainText = int(input("Plain-Text : "))
    prime_p, prime_q = checkPrime()
    n = prime_p * prime_q
    totient_func = (prime_p - 1) * (prime_q - 1)
    e  = coPrime(totient_func)
    public_key = (e, n)
    print("Public-Key :", public_key)
    
    inverse = extendedEuclidean(e, totient_func) # d = e^-1 mod (phi(n))
    d = inverse[1] % totient_func
    private_key = d
    print("Private-Key :", private_key)
    
    if(plainText < n):
        cipherText = rsaEncryption(plainText, e, n)
        print("\nCipher-Text :", cipherText)
    else:
        sys.exit("(Plain-text > n) ..... Invalid !!!")
        
    decipherText = rsaDecryption(cipherText, d, n) #d = private key
    print("\nDecipher-Text :", decipherText)
    
if __name__ == '__main__':
    main()
