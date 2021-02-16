# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:23:04 2021

@author: AshwinBalaji
"""
print("\nPLAY-FAIR CIPHER: DECRYPTION")
from collections import OrderedDict
import string as st
import time
keylist = []
textlist = []
character=None
character_1 = None
final_list = []

cap_alphabet_string = st.ascii_uppercase
cap_alphabet_list = list(cap_alphabet_string)
for i in cap_alphabet_list:
    if(i=='J'):#because i & j should be in same cell
        cap_alphabet_list.remove(i)

def get_key(keylist):
    key = input("Secret Key: ")
    key1 = "".join(key.split())
    if(key1.isalpha()):
        key = key1.upper()
        '''
        1. Set forming with key position unchanged
        2. If we use set(), then key values gets sorted which is not desirable
        '''
        keylist = list(OrderedDict.fromkeys(key))
        get_input(keylist, textlist)
    else:
        print("Unexpected input ... Please try again !!!")
        get_key(keylist)
    return

def get_input(keylist, textlist):
    text1 = input("Plain-text: ")
    text1 = "".join(text1.split())
    if(text1.isalpha()):
        text = text1.upper()
        textlist = list(text)
        get_keymatrix(keylist, textlist)
    else:
        print("Unexpected input ... Please try again !!!")
        get_input(keylist, textlist)
    return
 
def get_keymatrix(keylist, textlist):
    matrixlist1 = []
    columns = 5
    for i in keylist:
        matrixlist1.append(i)
    for j in cap_alphabet_list:
        matrixlist1.append(j)
    matrixlist = list(OrderedDict.fromkeys(matrixlist1))
    mstr = "".join(matrixlist)
    '''
    This part is very important as the string containing key string + remaining alphabets are added in the key matrix
    matrix = [['S', 'O', 'C', 'E', 'R'], 
              ['A', 'B', 'D', 'F', 'G'], 
              ['H', 'I', 'K', 'L', 'M'], 
              ['N', 'P', 'Q', 'T', 'U'], 
              ['V', 'W', 'X', 'Y', 'Z']]
    to get a matrix like this
    '''
    l = [list(mstr[i:i+columns]) for i in range(0, len(mstr), columns)]
    key_matrix = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    #print(key_matrix)
    text_split(textlist, key_matrix)
    return
'''
This function is to evalaute pair wise decide whether both character follow same row, same column, or diagonal case
'''
def evaluate(buffer, key_matrix):
    global character_1
    global character
    character = buffer[0]
    character_1 = buffer[1]
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i%5][j%5]==character):
                row = i
                column = j
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i%5][j%5]==character_1):
                row1 = i
                column1 = j             
    if(row==row1):
        rows(buffer, key_matrix)
    elif(column==column1):
        columns(buffer, key_matrix)
    else:
        diagonals(buffer, key_matrix)
    return
 
def rows(buffer,key_matrix):
    global final_list
    #Rule for the decryption of same row characters
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i][j] == character):
                final_list.append((key_matrix[i%5][(j-1)%5]))
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i][j] == character_1):
                final_list.append((key_matrix[i%5][(j-1)%5]))
    return

def columns(buffer, key_matrix):
    global character_1
    global character
    #Rule for the decryption of same column characters
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[j][i] == character):
                final_list.append((key_matrix[(j-1)%5][i%5]))
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[j][i] == character_1):
                final_list.append((key_matrix[(j-1)%5][i%5]))
    return

def diagonals(buffer, key_matrix):
    global character_1
    global character
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i%5][j%5]==character):
                row = i
                column = j
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i%5][j%5]==character_1):
                row1 = i
                column1 = j
    #Rule for the decryption if both characters are not in same row/column
    final_list.append(key_matrix[row][column1])
    final_list.append(key_matrix[row1][column])
    return

def text_split(textlist, key_matrix):
    global final_list
    buffer = []
    #splitting the string in the size of 2
    for i in range(0, len(textlist),2):
        buffer = textlist[i:i+2]
        evaluate(buffer, key_matrix)
    
#Driver-Code
get_key(keylist)
time.sleep(1)
print("\nDeciphering ......\n")
time.sleep(3)
print("Decrypted Successfully ......\n")
time.sleep(1.5)
val = 2
if (final_list[-1]=='X'):
    val=0#Case when X is bogus when Z is present in the  plain-text Ex: Plain-text=BUZZ, after substitution BUZXZX
if (final_list[-1]=='Z'):
    val=1#Case when Z is bogus when X is present in the  plain-text Ex: Plain-text=BUXX, after substitution BUXZXZ
for i in final_list:
    if(val==0 and i=='X'):
        final_list.remove(i)
    if(val==1 and i=='Z'):
        final_list.remove(i)
    if(val==2 and i=='X'): #This is a normal case when X is not added as bogus to make even length string Ex: Plain-text = Missizzi, new text = Misxsizxzi
        final_list.remove(i) 
    #Last case can be when plain-text is by default in even length and bogus character is not added            
decrypt = "".join(final_list)
print("Deciphered Text :", decrypt)

