# Transpose Matrix using Python
# Input: [[1,2,3],[4,5,6],[7,8,9]] | Output: [[1,4,7],[2,5,8],[3,6,9]]


rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("-------Your  Matrix is---------")
for n in matrix:
    print(n)

#result matrix of column*row  dimension

result =[[0 for i in range(rows)] for j in range(column)]

#transpose the matrix
for r in range(rows):
   
   for c in range(column):
       #here we are grabbing the row data of matrix and putting it in the column on the result
       result[c][r] = matrix[r][c]

print("Transpose matrix is: ")
for r in result:
    print(r)




def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for j in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed


row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
 
for i in range(row):          
    a =[]
    for j in range(column):
         a.append(int(input()))
    matrix.append(a)

print(transpose(matrix))