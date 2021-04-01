from fractions import Fraction

modulo = 16
print()
def echelon(matrix):
    
    if not matrix: return
    pivot = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    
    for row in range(rowCount):
        if pivot >= columnCount:
            return
        itr = row
        while matrix[itr][pivot] == 0:
            itr += 1
            if itr == rowCount:
                itr = row
                pivot += 1
                if columnCount == pivot:
                    return
                
        matrix[itr],matrix[row] = matrix[row],matrix[itr]
        pivotVal = matrix[row][pivot]
        matrix[row] = [finalVal / float(pivotVal) for finalVal in matrix[row]]
        
        for itr in range(rowCount):
            if itr != row:
                pivotVal = matrix[itr][pivot]
                matrix[itr] = [itrVal - pivotVal * rowVal for rowVal,itrVal in zip(matrix[row],matrix[itr])]
        pivot += 1
        
def extendedEuclidean(denominator, modulo):
    #global modulo
    if denominator == 0:
        return modulo, 0, 1
    else:
        gcd, x, y = extendedEuclidean(modulo % denominator, denominator)

        return gcd, y - (modulo // denominator) * x, x #or gcd, y - (modulo // denominator) * x, x

#matrix = [[3, 5, 7, 3], [1, 4, 13, 5], [2, 7, 3, 4]]

matrix = [[3, 5, 7, 3],
          [1, 4, 13, 5],
          [2, 7, 7, 4]]

 
echelon(matrix)
coordinateList = []
for row in matrix:
    row[-1] = Fraction(row[-1]).limit_denominator(10000)
    inter = row[-1]
    inter_cal = extendedEuclidean(Fraction(inter).denominator, modulo)
    inter_cal = (Fraction(inter).numerator * inter_cal[1]) % modulo
    coordinateList.append(inter_cal)
    print(row)

print()
print("X :", coordinateList[0], "Y :", coordinateList[1], "Z :", coordinateList[2])
#print(coordinateList)