import random
import numpy as np
from scipy.sparse import csr_matrix

rowd = int(input("What is the row dimension of your matrix? "))
cold = int(input("What is the column dimension of your matrix? "))
nnz = int(input("How many non-zero values are in your matrix? "))

rowpos = []
colpos = []
values = []
s = random.randint(0, rowd-1)
b = random.randint(0, cold-1)
rowpos.append(s)
colpos.append(b)
values.append(random.randint(1, 100))

size = rowd * cold
if nnz > size:
    print("Please enter a number of non-zero values that is less than or equal to the size of the matrix.")
    exit()


while len(rowpos) < nnz and len(colpos) < nnz:
    s = random.randint(0, rowd-1)
    b = random.randint(0, cold-1)
    inList = False
    for i in range(0, len(rowpos)):
        if s == rowpos[i] and b == colpos[i]:
            inList = True
    if inList == False:
        rowpos.append(s)
        colpos.append(b)
        values.append(random.randint(1, 100))

row = np.array(rowpos)
col = np.array(colpos)
data = np.array(values)

shape = (rowd, cold)
firstparam = (data, (row, col))
sparseMatrix = csr_matrix(firstparam, shape)
sparseMatrix_arr = sparseMatrix.toarray()

print("Here is your sparse matrix:")
print(sparseMatrix_arr)
print("Here is your sparse matrix in compressed sparse row format:")
print(sparseMatrix)