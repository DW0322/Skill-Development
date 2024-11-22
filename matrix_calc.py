def addition(matrix1, matrix2):

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result



def subtraction(matrix1, matrix2):

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result



def multiplication(matrix1, matrix2): 

    result = []
    for _ in range(len(matrix1)):
        row = []
        for _ in range(len(matrix2[0])):
            row.append(0)
        result.append(row)
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):  
            for k in range(len(matrix1[0])):  
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


#Example matrices
#Each list within the list is a row, every number in the row is a column. e.g matrix1[0][1] = 2 (from row 1 column 2)
matrix1 = [
    [1, 2], 
    [3, 4]
]

matrix2 = [
    [1, 2], 
    [3, 4]
]

#Uncomment below lines to test it out:

#result = addition(matrix1, matrix2)
#result = subtraction(matrix1, matrix2)
#result = multiplication(matrix1, matrix2)

for row in result:
    print(row)