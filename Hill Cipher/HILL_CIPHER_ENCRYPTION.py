# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:54:05 2021

@author: Ashwin Balaji
"""
import numpy as np
import string as st
import time as tm

print("HILL CIPHER: ENCRYPTION")

key_list = []
keycode_list = []
key_matrix = []
input_matrix = []
input_list = []
inputcode_list = []
split_matrix = []
split_multiply = []
result = []
result1 = []
result2 = []
result3 = []
length = None

cap_alphabet_string = st.ascii_uppercase
cap_alphabet_list = list(cap_alphabet_string)

'''
1. Taking input size of the KEY MATRIX from the user
2. Taking KEY STRING value from the user (Can be any string type excluding digits and string input can contain space also)
3. CHARACTER TO DIGIT and appending it in a list
4. Reshaping fucntion to adjust the KEY STRING input w.r.t the matrix size
'''

def get_key():
    key_size = int(input("Enter Key Size \n"))
    sq = key_size*key_size
    get_str = input("Please Input Key String (String size should be square of key size) \n")
    get_str = "".join(get_str.split())
    get_str = get_str.upper()
    #print(get_str)
    if (sq==len(get_str)):
        get_str = get_str.upper()
        key_list[:0] = get_str
        for x in key_list:
            keycode_list.append(ord(x)-65)
        key_matrix = np.array(keycode_list).reshape(key_size, key_size)
        #print(key_matrix)
        user_input(key_matrix,key_size)
    else:
        print("Invalid Input !!! Enter Again ....")
        get_key()

'''
1. Taking PLAIN TEXT from user which is to be encrypted
2. Note: Taken input should be in COLUMN order in a the INPUT MATRIX
3. Taking input and appending characters in the list using ORD()
4.  Reshaping the matrix as we wanted using reshaping array function
5. Suppose KEY MATRIX is 3X3 then INPUT MATRIX should also be in 3X3 with the input string in column order manner
'''
def user_input(key_matrix,key_size):
    in_str = input("Enter Plain Text\n")
    in_str = "".join(in_str.split())
    in_str = in_str.upper()
    #print(in_str)
    length = int(len(in_str)/key_size)
    #print(length)
    #print(in_str)
    if(((len(in_str))%key_size==0)):
        input_list = list(in_str)
        for x in input_list:
            inputcode_list.append(ord(x)-65)
        input_matrix = np.array(inputcode_list).reshape(key_size,length, order='F')#fortran order column major
    else:
        print("Alphabets are not in mutliples of Key Size !!! Try Again...")
        user_input(key_matrix,key_size)
    encryption(key_matrix,input_matrix,length)
    return

'''
1. Split the matrix in KEYSIZE X 1 to evaluate indiviually and multipy it with KEY MATRIX
2. Multiplied value in the matrix converted into MOD26
3. Converting Result into Alphabets
'''
def encryption(key_matrix,input_matrix,length):
    print('\nEncrypting ..... \n')
    tm.sleep(3)
    print('Encrypted Successfully \n')
    tm.sleep(1.5)
    for i in range(length):
        split_matrix = input_matrix[ : ,i]#column division
        split_multiply = np.dot(key_matrix,split_matrix)
        result = split_multiply%26#change
        result1 = result.tolist()
        #print(result1)
        for j in result1:
            result2.append(j)
    #Number to alphabets
    for x in result2:
        for y in range(len(cap_alphabet_list)):
            if (x == y):
                result3.append(cap_alphabet_list[y])
    lts = ''.join(map(str, result3))
    print("Ciphered Text: ",lts)
    return

#Driver-Code
get_key()