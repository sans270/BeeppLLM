import numpy as np

row = int(input("Enter the number of rows in your matrices: "))
col = int(input("Enter the number of columns in your matrices: "))

print("In what range do you want the random numbers in the first matrix to be? ") 
low1 = int(input("Enter the lowest number for the first matrix: "))
high1 = int(input("Enter the highest number for the first matrix: "))

print("In what range do you want the random numbers in the second matrix to be? ") 
low2 = int(input("Enter the lowest number for the first matrix: "))
high2 = int(input("Enter the highest number for the first matrix: "))


matrix1 = np.random.randint(low1, high1 + 1, (row, col))
matrix2 = np.random.randint(low2, high2 + 1, (row, col))


print("Your first randomly generated matrix of size ", row, "x", col, " is: ")
print(matrix1)
print("Your second randomly generated matrix of size ", row, "x", col, " is: ")
print(matrix2)
#Create lists to store the sum positions and values of the matrices
rowmatrixpositions = []
summatrixpositions = []
summatrixvalues = []


matrix3 = matrix1

for i in range(row):
    for j in range(col):
        num = (matrix1[i][j]) - (matrix2[i][j])
        if num == 0:
            matrix3[i][j] = 0
        else:
            matrix3[i][j] = num

        
print("The difference of your two matrices is: ")
print(matrix3)