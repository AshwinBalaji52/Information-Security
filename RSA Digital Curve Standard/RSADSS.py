# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 09:35:42 2021
@author: AshwinBalaji
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
    print(coprime_list)
    e  = random.choice(coprime_list)
    print(e)

    return e
    
def signing(private_key, n, plainText):
    signature = (plainText ** private_key) % n
    return signature

def verifying(public_key, signature, plainText):
    #public_key = (e, n)
    verify = (signature ** public_key[0]) % public_key[1]
    return verify
    

def main():
    print("\n\t\t\tRSA DIGITAL SIGNATURE STANDARD")
    plainText = int(input("Plain-Text : "))
    prime_p, prime_q = checkPrime()
    n = prime_p * prime_q
    totient_func = (prime_p - 1) * (prime_q - 1)
    print("totient-func :", totient_func)
    e  = coPrime(totient_func)
    print("e :", e)
    public_key = (e, n)
    print("\nPublic-Key :", public_key)
    
    inverse = extendedEuclidean(e, totient_func) # d = e^-1 mod (phi(n))
    d = inverse[1] % totient_func
    print("d :", d)
    private_key = d
    print("\nPrivate-Key :", private_key)
    
    signature = signing (private_key, n, plainText)
    print("\nSignature (S) :", signature)
    
    verify = verifying(public_key, signature, plainText)
    print("\nVerification (V) :", verify)
    
    if plainText == verify:
        print("\nSecured : [plainText == verify]")
    else:
        print("\nBreached : [plainText != verify]")
    
if __name__ == '__main__':
    main()