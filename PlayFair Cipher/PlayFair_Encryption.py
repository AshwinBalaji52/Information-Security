# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:23:04 2021

@author: AshwinBalaji
"""
print("\nPLAY-FAIR CIPHER: ENCRYPTION")
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
        for i in range(len(textlist)):
            if(textlist[i]=='J'):
                textlist[i]='I' #replacing J with I
        for i in range(len(textlist)):
            if (((ord(textlist[i-1]) - ord(textlist[i]))==0) and ((textlist[i])=='X')):
                insert_at = i
                insert_elements = ['Z'] #if continuous X character/bogus then we need to add new bogus as Z
                textlist[insert_at:insert_at] = insert_elements#inserting at the middle of two same characters
            elif ((ord(textlist[i-1]) - ord(textlist[i]))==0):
                insert_at = i
                insert_elements = ['X']#if no continuous X characters found then we can proceed normally
                textlist[insert_at:insert_at] = insert_elements#inserting at the middle of two same characters
        if(len(textlist)%2!=0 and textlist[-1]!='X'):#bogus character X at the end of the string to make even length if no continuous X character found
            textlist.append('X')#bogus character
        elif(len(textlist)%2!=0 and textlist[-1]=='X'):#bogus character Z at the end of the string to make even length if continuous X character found
            textlist.append('Z')#bogus character Ex: Plain-text = Posix, new substituted text = Posixz
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
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i][j] == character):
                #Rule for the encryption of same row characters
                final_list.append((key_matrix[i%5][(j+1)%5]))
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[i][j] == character_1):
                final_list.append((key_matrix[i%5][(j+1)%5]))
    return

def columns(buffer, key_matrix):
    global character_1
    global character
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[j][i] == character):
                #Rule for the encryption of same column characters
                final_list.append((key_matrix[(j+1)%5][i%5]))
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if(key_matrix[j][i] == character_1):
                final_list.append((key_matrix[(j+1)%5][i%5]))
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
    #Rule for the encryption if both characters are not in same row/column
    final_list.append(key_matrix[row][column1])
    final_list.append(key_matrix[row1][column])
    return

def text_split(textlist, key_matrix):
    global final_list
    buffer = []
    for i in range(0, len(textlist),2):
        #splitting the string in the size of 2
        buffer = textlist[i:i+2]
        evaluate(buffer, key_matrix)
    
#Driver-Code
get_key(keylist)
time.sleep(1)
print("\nEnciphering ......\n")
time.sleep(3)
print("Encrypted Successfully ......\n")
time.sleep(1.5)
encrypt = "".join(final_list)
print("Ciphered Text :", encrypt)

