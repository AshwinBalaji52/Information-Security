# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:54:05 2021

@author: Ashwin Balaji
"""
import numpy as np
import string as st
import time as tm

print("HILL CIPHER: DECRYPTION")

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
key_inv_matrix = []
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
    if (sq==len(get_str)):
        get_str = get_str.upper()
        key_list[:0] = get_str
        for x in key_list:
            keycode_list.append(ord(x)-65)
        #reshaping function can make matrix as desired size we want
        key_matrix = np.array(keycode_list).reshape(key_size, key_size) 
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
    length = int(len(in_str)/key_size)
    if(((len(in_str))%key_size==0)):
        input_list = list(in_str)
        for x in input_list:
            inputcode_list.append(ord(x)-65)
        input_matrix = np.array(inputcode_list).reshape(key_size,length, order='F')#fortran order column major
    else:
        print("Alphabets are not in mutliples of Key Size !!! Try Again...")
        user_input(key_matrix,key_size)
    decryption(key_matrix,input_matrix,length)
    return
'''
Decryption: Split multiply will break input matrix into (Keysize X 1) to evaluate individually
'''
def decryption(key_matrix,input_matrix,length):
    for i in range(length):
        split_matrix = input_matrix[ : ,i]#column division
        key_inv_matrix = inv_matrix(key_matrix)
        split_multiply = np.dot(key_inv_matrix,split_matrix)
        result = split_multiply%26#change
        result1 = result.tolist()
        for j in result1:
            result2.append(j)
    for x in result2:
        for y in range(len(cap_alphabet_list)):
            if (x == y):
                result3.append(cap_alphabet_list[y])
    lts = ''.join(map(str, result3))
    print("Deciphered Text: ",lts)
    return

'''
Inverse mod function may identify that the given key can be used for decryption or not
'''
def inv_mod(a): 
    a = a % 26
    for x in range(1, 26): 
        if ((a * x) % 26 == 1): 
            return x 
    return 1
'''
1. Evaluating inverse of a matrix.
2. Determining whether matrix can be decrypted or not w.r.t KEY
        P = (K^-1)Cmod26 #C= cipher text, K^-1 = Key inverse matrix, P = plain text
'''
def inv_matrix(key_matrix): 
    det = int(np.linalg.det(key_matrix))#edeterminant function
    inverse_mod = inv_mod(det)
    modulo26det = det%26
    #Check if inverse possible or not
    if (det==0 or (modulo26det%2 == 0) or (modulo26det%13 == 0)):
            print("Enter a Valid Key, Key Matrix is Not Inveritble or determinant has common factors with modular base.")
            get_key()
    else:
        key_inv_matrix = (np.linalg.inv(key_matrix)*det)%26 #(INV|M|*det = ADJ(Matrix) and %26 gives negative elements in adj(m) to positive
        key_matrix1 = (inverse_mod*key_inv_matrix)%26
        print('\nDecrypting ..... \n')
        tm.sleep(3)
        print('Decrypted Successfully \n')
        tm.sleep(1.5)
        return(key_matrix1)
    
#Driver-Code
get_key()