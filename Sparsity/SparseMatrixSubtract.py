import random
import numpy as np
from scipy.sparse import csr_matrix
from scipy import sparse


#Get row and column dimensions, and two numbers of nonzeros
rowd = int(input("What is the row dimension of your matrix? "))
cold = int(input("What is the column dimension of your matrix? "))
fnnz = int(input("How many non-zero values are in your first matrix? "))
snnz = int(input("How many non-zero values are in your second matrix? "))

#Function to create the matrix
def create_matrix(rowd, cold, nnz):
    #Create empty lists
    rowpos = []
    colpos = []
    values = []
    #Generate the first random row and column positions and value and add to lists
    s = random.randint(0, rowd-1)
    b = random.randint(0, cold-1)
    rowpos.append(s)
    colpos.append(b)
    values.append(random.randint(1, 100))

    #Fine size of matrix
    size = rowd * cold
    #Check if number of nonzeros is greater than size- will not work
    if nnz > size:
        print("Please enter a number of non-zero values that is less than or equal to the size of the matrix.")
        exit()

    #Generate the rest of the random row and column positions and values and add to lists
    while len(rowpos) < nnz and len(colpos) < nnz:
        #Generate random row and column positions and value
        s = random.randint(0, rowd-1)
        b = random.randint(0, cold-1)
        #Create a check to make sure that the position is not already in the list
        inList = False
        #Check if the position is already in the list
        for i in range(0, len(rowpos)):
            if s == rowpos[i] and b == colpos[i]:
                inList = True
        #If it is not in the list, add the positions and value to the lists
        if inList == False:
            rowpos.append(s)
            colpos.append(b)
            values.append(random.randint(1, 100))

    #Convert lists to arrays
    row = np.array(rowpos)
    col = np.array(colpos)
    data = np.array(values)

    #Create the matrix using the shape, data, row positions, and column positions
    shape = (rowd, cold)
    firstparam = (data, (row, col))
    sparseMatrix = csr_matrix(firstparam, shape)
    sparseMatrix_arr = sparseMatrix.toarray()
    return sparseMatrix_arr, sparseMatrix

print("Here is your first sparse matrix:")
#Call the function to create the first matrix using the row and column dimensions and first number of nonzeros
sparseMatrix_arr, sparseMatrix = create_matrix(rowd, cold, fnnz)
print(sparseMatrix_arr)
print("Here is your first sparse matrix in compressed sparse row format:")
#Print the first matrix in compressed sparse row format
print(sparseMatrix)
print('\n')
print("Here is your second sparse matrix:")
#Call the function to create the second matrix using the row and column dimensions and second number of nonzeros
sparseMatrix_arr2, sparseMatrix2 = create_matrix(rowd, cold, snnz)
print(sparseMatrix_arr2)
print("Here is your second sparse matrix in compressed sparse row format:")
#Print the second matrix in compressed sparse row format
print(sparseMatrix2)
print('\n')

#Create lists to store the sum positions and values of the matrices
rowmatrixpositions = []
summatrixpositions = []
summatrixvalues = []
for i in range(0, rowd):
    #Get each row of the matrices based on the index
    row = sparseMatrix.getrow(i)
    row2 = sparseMatrix2.getrow(i)
    #Get the positions and values of each row
    position1 = row.indices
    position2 = row2.indices
    values1 = row.data
    values2 = row2.data
    fi = 0
    si = 0
    #Loop while the two counts fi and si are less than the number of nonzeros in the rows
    while fi < row.getnnz() and si < row2.getnnz():
        #Check if one of the rows has no nonzeros- if it does, just add the row that has nonzeros
        if len(position1) == 0:
            for j in range(1, len(position2)):
                summatrixpositions.append(position2[j])
                summatrixvalues.append(values2[j])
                rowmatrixpositions.append(i)
            break
        #Check if one of the rows has no nonzeros
        if len(position2) == 0:
            for b in range(1, len(position1)):
                summatrixpositions.append(position1[b])
                summatrixvalues.append(values1[b])
                rowmatrixpositions.append(i)
            break
        #Check if the positions are equal- then add the values together and add the position to the sum matrix, increase fi and si by one
        if position1[fi] == position2[si]:
            x = values1[fi] - values2[si]
            if x == 0:
                continue
            else:
                summatrixvalues.append(round(x, 2))
                summatrixpositions.append(position1[fi])
                rowmatrixpositions.append(i)
                fi = fi + 1
                si = si + 1
        else:
            #If they are not equal, check which position is smaller and add that value and position to the sum matrix, increase fi or si by one
            if position1[fi] < position2[si]:
                summatrixpositions.append(position1[fi])
                summatrixvalues.append(round(values1[fi], 2))
                rowmatrixpositions.append(i)
                fi = fi + 1
                continue

            if position2[si] < position1[fi]:
                summatrixpositions.append(position2[si])
                summatrixvalues.append(round(values2[si], 2))
                rowmatrixpositions.append(i)
                si = si + 1
    #Check if fi or si is less than the number of nonzeros in the row- if it is, add the rest of the values and positions to the sum matrix
    while fi < row.getnnz():
        print(fi)
        summatrixpositions.append(position1[fi])
        summatrixvalues.append(round(values1[fi], 2))
        rowmatrixpositions.append(i)
        fi = fi + 1
    while si < row2.getnnz():
        summatrixpositions.append(position2[si])
        summatrixvalues.append(round(values2[si], 2))
        rowmatrixpositions.append(i)
        si = si + 1


#Create the sparse matrix using the sum positions, values, and the row and column dimensions
addedmatrix = sparse.csr_matrix((summatrixvalues,(rowmatrixpositions,summatrixpositions)),shape=(rowd,cold))

#Print the sum matrix
print("Here is your added sparse matrix:")
print(addedmatrix.toarray())