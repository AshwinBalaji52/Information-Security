# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:41:06 2021

@author: Ashwin Balaji
"""
print("VIGENERE CIPHER: DECRYPTION")

import time as tm

key_list = []

def key(key_list):
    get_key = input("Please Input Key A..Z/a..z \n")
    get_key1 = "".join(get_key.split())#remove space
    if(get_key1.isalpha()==True):
        get_key = get_key1.upper()
        length_key = len(get_key)
        key_list[:0] = get_key
        get_text(key_list, length_key)
    else:
        print("Please Input Valid Key \n")
        key(key_list)
    return

def get_text(key_list, length_key):
    input_list = []
    get_str = input("Please Input Encrypted Text A..Z/a..z \n")
    get_str1 = "".join(get_str.split())
    if(get_str1.isalpha()==True):
        get_str = get_str1.upper()
        length_str = len(get_str)
        input_list[:0] = get_str
        merge(input_list, key_list, length_str, length_key)
    else:
        print("Please Input Valid Text \n")
        get_text(key_list, length_key)
    return

def merge(input_list, key_list, length_str, length_key):
    key_result = []
    if(length_str > length_key):
        for i in range(length_str-length_key):
            key_list.append(key_list[i % length_key])
        key_result = key_list.copy()
    else:
        for i in range(len(input_list)):
            key_result.append(key_list[i])
    encryption(key_result, input_list, length_str)     
    return

def encryption(key_result, input_list, length_str):
    decipher_text = []
    for i in range(length_str):
        character = (ord(input_list[i]) - ord(key_result[i]) + 26)%26
        character += ord('A')#this avoids hexadecimal error when we use chr(character) in LOC
        decipher_text.append(chr(character))
    dts = "".join(decipher_text)
    print("\nDecryption Initiated \n")
    tm.sleep(2)
    print("Deciphering ...... \n")
    tm.sleep(4)
    print("Deciphered Text: ",dts)
    return

#Driver-Code
key(key_list)

