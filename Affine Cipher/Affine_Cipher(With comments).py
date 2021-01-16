# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 23:11:01 2021

@author: Ashwin Balaji
"""
#class
import string as st
import time as tm

#Global
key1_domain = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]#Z26*
key2_domain = []#Z26
input_text = []#input txt in list form
output_text = []#output txt in list form
input_index_text = []#containing index value i.e., P value of the user string
output_index_text = []#containing index value of encoded string/list
get_k1 = None
get_k2 = None
get_str = None
encode = None
decode = None
value =  None

#to extract capital letters
cap_alphabet_string = st.ascii_uppercase
cap_alphabet_list = list(cap_alphabet_string)

#to extract index of capital letters to a new list()
for n in range(len(cap_alphabet_list)):
     key2_domain.append(int(n))
'''
can be done like this also
for i  in range(0,26):
    key3_domain.append(i)
'''
'''
print(cap_alphabet_list.index(n)) print index values of a list
new_alphabet_list = cap_alphabet_list.copy() if you want to copy
Used copy() instead of just '=' because if we try to append a data in the list after performing
list 2 = list 1, then new and old both will containt new data, to avoid this we use copy()
'''
print('AFFINE CIPHER: ENCRYPTION & DECRYPTION')
def get_key():
        get_k1 = int(input("Enter K1 from 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 \n"))
        if get_k1 in key1_domain:
            get_k2 = int(input("Enter K2 from 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 \n"))
            if get_k2 in key2_domain:
                print('\nYour chosen Key(K1,K2) values are: ',(get_k1,get_k2))
                
                #value = choice(value)
                #encryption(get_k1,get_k2)
                #decryption(get_k1,get_k2)
                
                choice()
                
            else:
                print("Please Try Again")
                get_input()
        else:
            print("Please Try Again")
            get_input()

def get_text():
    get_str = input("Enter Plain Text: ")
    if (get_str.isupper()):
        input_text[:0] = get_str #convert string to list form
        get_index() #input bydefault takes arguments in string format, we need to typecaste if need*
    else:
        chng_str = get_str.upper()
        input_text[:0] = chng_str
        get_index()

# fetch index of the user-text w.r.t cap_alphabets, for ex: HELLO, in which "H" = 7th index in cap_alphabets list
def get_index():
    for x in input_text:
        if x in cap_alphabet_list and x not in input_index_text:
            z = ord(x)-65
            input_index_text.append(z)
    get_key()

#Encryption
def encryption(a,b):
    print('\nEncrypting ..... \n')
    tm.sleep(3)
    print('Encrypted Successfully \n')
    tm.sleep(1.5)
    for iterator in range(len(input_index_text)):
        encode = input_index_text[iterator]
        calculate = ((encode*a)+b)%26
        output_index_text.append(calculate)
    #print(output_index_text)
    #print(''.join(map(chr,output_index_text)))
    #for itr in output_index_text:
     #   output_text.append(chr(itr))#why this function not mapping to ascii char rather it's mapping to non-printable python characters
    #output_text = [chr(itr) for itr in output_index_text]
    #print(output_text)
    for x in output_index_text:
        for y in range(len(cap_alphabet_list)):
            if (x == y):
                output_text.append(cap_alphabet_list[y])
    lts = ''.join(map(str, output_text)) #convert list to string ' '.join([str(elem) for elem in s]) can also be done
    print("Encrypted Text: ",lts)
    return 0

#Decryption
def decryption(a,b):
    print('\nDecrypting ..... \n')
    tm.sleep(3)
    print('Decrypted Successfully \n')
    tm.sleep(1.5)
    for iterator in range(len(input_index_text)):
        decode = input_index_text[iterator]
        calculate = ((decode-b)*gcd(a))%26
        output_index_text.append(calculate)
    for x in output_index_text:
        for y in range(len(cap_alphabet_list)):
            if (x == y):
                output_text.append(cap_alphabet_list[y])
    lts = ''.join(map(str, output_text)) #conevert list to string ' '.join([str(elem) for elem in s]) can also be done
    print("Decrypted Text: ",lts)
    return 0
#GCD calculation
def gcd(a):
    for inv in range(26):
        if ((7*inv)%26==1):
            return inv
get_text()
    
        
