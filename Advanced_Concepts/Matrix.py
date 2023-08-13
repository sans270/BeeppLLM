import numpy as np

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
print("In what range do you want the random numbers to be? ") 
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

matrix = np.random.uniform(low, high + 1, (row, col))
print("Your randomly generated matrix of size ", row, "x", col, " is: ")
print(matrix)