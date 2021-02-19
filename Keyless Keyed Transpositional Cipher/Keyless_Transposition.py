# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:41:46 2021
@author: Ashwin Balaji
"""
import string
import random
import time

print("\nKEYLESS TRANSPOSITION ENCRYPTION & DECRYPTION: RAIL-FENCE CIPHER")

text = None
keysize = None
counter = 0

'''
This alphabet list is used in filler() to complete matrix None spaces with random characters
'''
cap_alphabet_string = string.ascii_uppercase
cap_alphabet_list = list(cap_alphabet_string)

def get_input():
    
    '''
    Point to remember 1: Key Matrix size here will decide number of column
    Point to remember 2: Try to input plain-text to the sqaure of size of key matrix size
                        if not filler function will try to add bogus character to fill empty matrix cells
    Point to remember 3: filler will fill only the last ROW (logically) in N x N matrix 
                        so in Nth row (i.e., in last row) try to fill atleast one character such that remaining N-1 characters
                        will be taken care of filler()
    '''
    keysize = int(input(("Key Matrix Size: ")))
    
    text = input("Plain-Text: ")
    text1 = "".join(text.split())
    
    if(text1.isalpha()):
        text = text1.upper()
        
    #Logically text length must not be greatr than key_matrix size 
    if((keysize*keysize)>=len(text)):
        make_matrix(keysize,text)
    else:
        print("Unexpected Input or Length condition not satisfied ..... Try Again !!!")
        get_input()
    return
def make_matrix(keysize,text):
    
    columns = keysize #columns
    
    '''
    This part will break the plain text into matrix form
    Also, print(len(key_matrix)) #giving number of rows len(matrix gives number of rows)
    So now we have column size (provided by user and row size (length of matrix)
    '''
    l = [list(text[i:i+columns]) for i in range(0, len(text), columns)]
    key_matrix = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    
    filler(key_matrix, keysize)
    return
'''
if matrix is N x N filler can only work for Nth row and atleast in Nth row 1 position is filled
Such that all other N-1 positions are filled with random alphabets to complete the matrix size
And during decryption automatically the bogus characters (if any) will get eliminated
'''  
def filler(key_matrix,keysize):
    
    global counter
    
    for i in range(keysize):
        for j in range(len(key_matrix)):
            if(key_matrix[i][j]==None):
                
                #counter to keep track of #bogus_characters added in the matrix
                counter+=1
                key_matrix[i][j] = random.choice(cap_alphabet_list)
                
    encryption(key_matrix,keysize)
    return

def encryption(key_matrix, keysize):
    
    global counter
    encrypted_list = []
    
    '''
    Since, Plain-text is filled row wise in the matrix, so rail fence cipher will now print the 
    encrypted text column-wise (Transposed)
    '''
    for i in range(keysize):
        for j in range(len(key_matrix)):
            if(key_matrix[j][i]!=None):
                encrypted_list.append(key_matrix[j][i])
            else:
                pass
            
    ltse = "".join(encrypted_list)
    
    time.sleep(1)
    print("\nNow Proceeding with Encryption process ...... ")
    time.sleep(2)
    print("\nEncrypted Text: ",ltse)
    time.sleep(1)
    
    decryption(ltse, keysize)
    return

def decryption(ltse, keysize):
    
    global counter
    decrypted_list = []
    columns = keysize
    
    print("\nNow Proceeding with Decryption process ...... ")
    time.sleep(2)

    '''
    This part will break the encrypted text into matrix form
    Also, print(len(key_matrix)) #giving number of rows len(matrix gives number of rows)
    So now we have column size (provided by user and row size (length of matrix)
    '''
    l = [list(ltse[i:i+columns]) for i in range(0, len(ltse), columns)]
    key_matrix1 = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    
    '''
    Since, encrypted is filled column-wise in the matrix, so rail fence cipher will now print the 
    decrypted/plain text row-wise (Transposed again)
    '''    
    for i in range(keysize):
        for j in range(len(key_matrix1)):
            if(key_matrix1[j][i]!=None):
                decrypted_list.append(key_matrix1[j][i])
            else:
                pass
            
    ltsd = "".join(decrypted_list)
    
    if (counter!=0):
        
        #removing number filler/bogus characters using a counter
        ltsd = ltsd[:-counter]
    print("\nDecrypted Text: ",ltsd)
    return

#Driver-Code
get_input()

