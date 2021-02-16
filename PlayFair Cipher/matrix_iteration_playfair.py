
matrix = [['S', 'O', 'C', 'E', 'R'], 
          ['A', 'B', 'D', 'F', 'G'], 
          ['H', 'I', 'K', 'L', 'M'], 
          ['N', 'P', 'Q', 'T', 'U'], 
          ['V', 'W', 'X', 'Y', 'Z']]
final_list = []
def evaluate(x):
    character = x[0]
    character_1 = x[1]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i%5][j%5]==character):
                row = i
                column = j
                #print(i,j)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i%5][j%5]==character_1):
                row1 = i
                column1 = j
                #print(i,j)               
    if(row==row1):
        #print("same row",x)
        rows(x,character,character_1)
    elif(column==column1):
        #print("same column",x)
        columns(x,character,character_1)
    else:
        #print("Diagonal case",x)
        diagonals(x,character,character_1)
    return
 
def rows(x,character,character_1):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == character):
                #print(character)
                final_list.append((matrix[i%5][(j-1)%5]))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == character_1):
                #print(character_1)
                final_list.append((matrix[i%5][(j-1)%5]))
    #print(final_list)
    return

def columns(x,character,character_1):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[j][i] == character):
                #print(character)
                final_list.append((matrix[(j-1)%5][i%5]))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[j][i] == character_1):
                #print(character_1)
                final_list.append((matrix[(j-1)%5][i%5]))
    #print(final_list)
    return

def diagonals(x,character,character_1):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i%5][j%5]==character):
                row = i
                column = j
                #print(i,j)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i%5][j%5]==character_1):
                row1 = i
                column1 = j
                #print(i,j)
    final_list.append(matrix[row][column1])
    final_list.append(matrix[row1][column])
    #print(final_list)
    return

string = "HAIVHP"
l = list(string)
x = []
for i in range(0, len(l),2):
    x = l[i:i+2]
    print(x)
    evaluate(x)
print(final_list)




    
