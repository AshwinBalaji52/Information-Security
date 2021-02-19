from random import shuffle
counter=1
#index = None
index = []
#indexlist = []
decrypt_list = []
intermediate = []
words = ['B', 'A', 'L', 'K','J','I']
newwords = words.copy() # Copy words
shuffle(newwords) # Shuffle newwords

for i in range(len(words)):
    for j in range(len(newwords)):
        if(words[i]==newwords[j]):
            index.append(j)

print("Original list: ",words)  
#zipped_lists = zip(index, newwords)
#print(zipped_lists)
'''
sorted_zipped_lists = sorted(zipped_lists)
decrypt_list = [element for _, element in sorted_zipped_lists]  
'''
print("Index: ",index)
print("New list: ",newwords)

#print("Decrypted List :", decrypt_list)
for i in range(len(newwords)):
    intermediate.append((i,newwords[i]))
print(intermediate)

res = [tuple for x in index for tuple in intermediate if tuple[0] == x]
#print(res) 
for i in res:
    tuples = i
    alphabet = tuples[1]
    decrypt_list.append(alphabet)
print(res)
print(decrypt_list)




