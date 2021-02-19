# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:41:46 2021
@author: Ashwin Balaji
"""
import time
counter = 1
index_list = []
encrypt_list = []
decrypt_list = []
keysize = 0
print("\nKEYED TRANSPOSITION ENCRYPTION & DECRYPTION")

'''
Input Function to obtain block size and Plain-text from user and
'''
def get_input():
    
    global keysize
    global index_list
    
    keysize = int(input(("Block Size: ")))#it will be used to decide block size
    
    print("Block values from 1 to",keysize,"without repetition")
    for i in range(keysize):
        element = int(input("Value :"))
        element-=1
        index_list.append(element)
    '''
    Point to remember: Plain-text should be in multiples of block size so that no NULL values are stores in further process
    '''
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
    
    '''
    To break the plain text w.r.t Block size and storing it in a matrix
    '''
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
    
    #Destacking row wise from the Text-matrix to proceed with encryption row by row
    #Copy() is used so that destacked row doesn't get modified when conversion occurs
    convert = destack.copy() # Copy words
    
    '''
    This part is important as this part converts/sorts list w.r.t to block values
    obtained from the user
    '''
    zipped_lists = zip(index_list, convert)
    sorted_zipped_lists = sorted(zipped_lists)
    convert = [element for _, element in sorted_zipped_lists] 
    
    #Appending encrypted rows one by one into encrypt_list
    for i in range(len(convert)):
        encrypt_list.append(convert[i])
        
    if(length==counter):
        time.sleep(1)
        print("\nNow proceeding with Encryption process ......")
        time.sleep(2)
        ltse = "".join(encrypt_list)
        print("\nEncrypted Text:",ltse)
        text_split_decrypt(encrypt_list)
    return

def text_split_decrypt(encrypt_list):
    
    global keysize
    global counter
    
    columns = keysize #columns
    
    '''
    To break the plain text w.r.t Block size and storing it in a matrix
    '''
    l = [list(encrypt_list[i:i+columns]) for i in range(0, len(encrypt_list), columns)]
    text_matrix = [s if len(s) == columns else s+[None]*(columns-len(s)) for s in l]
    
    length = len(text_matrix)
    
    for i in text_matrix:
        decryption(i, length)
        counter-=1
    return

def decryption(destack, length):
    
    global counter
    intermediate_list=[]
    
    '''
    Tuple is created like (Sequential_Index , encrypted_alphabet)
    This tuple gives the new index list (Which is basically the sequential index of the encrypted alphabets)
    Such tuple pair is obtained and stored in intermediate_list
    '''
    for i in range(len(destack)):
        intermediate_list.append((i,destack[i]))
        
    '''
    This part actually maps the new (sequential_index , encrypted_list) with the previous index obtained from the user
    '''
    result = [tuple for x in index_list for tuple in intermediate_list if tuple[0] == x]
    
    #Obtaning one by one alphabets (which is now again converted to decrypted form)
    for i in result:
        tuples = i
        alphabet = tuples[1]
        decrypt_list.append(alphabet)
        
    if(counter==1):
        time.sleep(1)
        print("\nNow proceeding with Decryption process ......")
        time.sleep(2)
        ltsd = "".join(decrypt_list)
        print("\nDecrypted Text:",ltsd)
    return

#Driver-Code
get_input()