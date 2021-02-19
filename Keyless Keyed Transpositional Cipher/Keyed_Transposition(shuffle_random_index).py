# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:41:46 2021

@author: dell
"""
'''
Doesn't work fine if the first block of letters are in repetition, otherwise in all cases it works fine'
this doesn't take block index from human rather shuffle function is used to get index, as it changes everytime'
'''
from random import shuffle
from collections import OrderedDict
counter = 1
index_list = []
encrypt_list = []
decrypt_list = []
keysize = 0
print("\nKEYED TRANSPOSITION CIPHER")
def get_input():
    global keysize
    keysize = int(input(("Block Size: ")))#it will be used to decide number of columns
    text = input("Plain-Text: ")
    text1 = "".join(text.split())
    if(text1.isalpha()):
        text = text1.upper()
        textlist = list(text)
        if((len(textlist)%keysize)==0):
            text_split_encrypt(textlist)
        else:
            print("\nLength of text is not equal to the multiples of block size ..... Try Again !!!")
            get_input()
    else:
        print("\nUnexpected Input or Length of text is not equal to the multiples of block size ..... Try Again !!!")
        get_input()
    return

def text_split_encrypt(textlist):
    global counter
    global keysize
    columns = keysize #columns
    l = [list(textlist[i:i+columns]) for i in range(0, len(textlist), columns)]
    text_matrix = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    length = len(text_matrix)
    for i in text_matrix:
        encryption(i, length)
        counter+=1
    return

def encryption(destack, length):
    global counter
    global index_list
    
    convert = destack.copy() # Copy words
    index=[]
    if (counter==1):
        shuffle(convert) # Shuffle newwords
        
        for i in range(len(destack)):
            for j in range(len(convert)):
                if(destack[i]==convert[j]):
                    index.append(j)
                    index_list = list(OrderedDict.fromkeys(index))
        print(index_list)
        for i in range(len(convert)):
            encrypt_list.append(convert[i])
            
    if(counter>1):
        zipped_lists = zip(index_list, convert)
        sorted_zipped_lists = sorted(zipped_lists)
        convert = [element for _, element in sorted_zipped_lists] 
        for i in range(len(convert)):
            encrypt_list.append(convert[i])
    if(length==counter):
        ltse = "".join(encrypt_list)
        print("\nEncrypted Text:",ltse)
        text_split_decrypt(encrypt_list)
    return

def text_split_decrypt(encrypt_list):
    global keysize
    global counter
    columns = keysize #columns
    l = [list(encrypt_list[i:i+columns]) for i in range(0, len(encrypt_list), columns)]
    text_matrix = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    print("\n",text_matrix)
    length = len(text_matrix)
    for i in text_matrix:
        decryption(i, length)
        counter-=1
    return

def decryption(destack, length):
    global counter
    intermediate_list=[]
    result=[]
    global index_list
    for i in range(len(destack)):
        intermediate_list.append((i,destack[i]))
    #based on index new sort
    result = [tuple for x in index_list for tuple in intermediate_list if tuple[0] == x]
    print(intermediate_list)
    for i in result:
        tuples = i
        alphabet = tuples[1]
        decrypt_list.append(alphabet)
    #decrypt_list
    print(result)
    if(counter<=1):
        ltsd = "".join(decrypt_list)
        print("\n",decrypt_list)
        print("\n",index_list)
        print("\nDecrypted Text:",ltsd)
    return

get_input()