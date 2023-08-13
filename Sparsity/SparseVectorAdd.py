import random
from random import sample

total = int(input("What is your total number of entries?  "))
sparse1 = float(input("What is your sparsity ratio for your first vector? (decimal)  "))
sparse2 = float(input("What is your sparsity ratio for your second vector? (decimal)  "))

actual1 = int(total*sparse1)
actual2 = int(total*sparse2)

position1 = []
position2 = []


actual1list = []
actual2list = []



for i in range(1, total-1):
    actual1list.append(i)
for i in range(1, total-1):
    actual2list.append(i)

#position1.append(sample(actual1list, actual1))
position1 = sample(actual1list, actual1)
#position2.append(sample(actual2list, actual2))
position2 = sample(actual2list, actual2)

position1 = sorted(position1)
position2 = sorted(position2)


values1 = []
values2 = []

for i in range(0, actual1):
    values1.append(round(random.uniform(10, 100), 2))

for i in range(0, actual2):
    values2.append(round(random.uniform(10, 100), 2))

print("This is your first sparse vector: ")
print("Positions: ", position1)
print("Values: ", values1)
print("This is your second sparse vector: ")
print("Positions: ", position2)
print("Values: ", values2)

fi = 0
si = 0

sumvectorpositions = []
sumvectorvalues = []

while fi < len(position1) and si < len(position2):
    if position1[fi] == position2[si]:
        x = values1[fi] + values2[si]
        sumvectorvalues.append(round(x, 2))
        sumvectorpositions.append(position1[fi])
        fi = fi + 1
        si = si + 1
    else:
        if position1[fi] < position2[si]:
            sumvectorpositions.append(position1[fi])
            sumvectorvalues.append(round(values1[fi], 2))
            fi = fi + 1
        if position2[si] < position1[fi]:
            sumvectorpositions.append(position2[si])
            sumvectorvalues.append(round(values2[si], 2))
            si = si + 1
while fi < len(position1):
    sumvectorpositions.append(position1[fi])
    sumvectorvalues.append(round(values1[fi], 2))
    fi = fi + 1
while si < len(position2):
    sumvectorpositions.append(position2[si])
    sumvectorvalues.append(round(values2[si], 2))
    si = si + 1

print("This is your two sparse vectors added:")
print("Positions:  ", sumvectorpositions)
print("Values:  ", sumvectorvalues)
    