import random

total = int(input("What is your total number of entries?"))
sparse1 = float(input("What is your sparsity ratio for your first vector? (decimal)  "))
sparse2 = float(input("What is your sparsity ratio for your second vector? (decimal)  "))

actual1 = int(total*sparse1)
actual2 = int(total*sparse2)

position1 = []

for i in range(0, actual1):
    position1.append(random.randint(1, total-1))


position2 = []

for i in range(0, actual2):
    position2.append(random.randint(1, total-1))

position1.sort()
position2.sort()


values1 = []
values2 = []

for i in range(0, actual1):
    values1.append(round(random.sample(10, 100), 2))

for i in range(0, actual2):
    values2.append(round(random.sample(10, 100), 2))

print("This is your first sparse vector: ")
print("Positions: ", position1)
print("Values: ", values1)
print("This is your second sparse vector: ")
print("Positions: ", position2)
print("Values: ", values2)