import math
print("This program will take two homework grades, two test grades, and a participation grade (in file)")
f=open('Mine_Grades.txt',"r")

lines=f.readlines()

numrows = len(lines)
column1=[]
column2=[]
column3=[]
column4=[]
column5=[]
column6no=[]
count = 0

for line in lines:
        column1.append(line.split(' ')[0])
        count = count + 1
f.close()

for line in lines:
        column2.append(line.split(' ')[1])
        count = count + 1
f.close()

for line in lines:
        column3.append(line.split(' ')[2])
        count = count + 1
f.close()

for line in lines:
        column4.append(line.split(' ')[3])
        count = count + 1
f.close()

for line in lines:
        column5.append(line.split(' ')[4])
        count = count + 1
f.close()

for line in lines:
        column6no.append(line.split(' ')[5])
        count = count + 1
f.close()

column6 = []
for sub in column6no:
    column6.append(sub.replace("\n", ""))

print("Please enter the weights for tests, homework, and participation.")
tests = float(input("What is the weight for tests as a decimal?"))
homework = float(input("What is the weight for homework as a decimal?"))
participation = float(input("What is the weight for participation as a decimal?"))

homeworkgradelist = []
hwcounter = 0


for i in range(1, numrows+1):
    value = (int(column2[hwcounter])+int(column3[hwcounter]))/2
    total = homework*value
    homeworkgradelist.append(total)
    hwcounter = hwcounter + 1
testgradelist = []
testcounter = 0


for i in range(1, numrows+1):
    tvalue = (int(column4[testcounter])+int(column5[testcounter]))/2
    ttotal = tests*tvalue
    testgradelist.append(ttotal)
    testcounter = testcounter + 1

partgradelist = []
partcounter = 0


for i in range(1, numrows+1):
    pvalue = int(column6[partcounter])
    ptotal = participation * pvalue
    partgradelist.append(ptotal)
    partcounter = partcounter + 1


finalgradelist = []
counter = 0
for i in range(0, numrows):
        finalgrade = homeworkgradelist[counter] + testgradelist[counter] + partgradelist[counter]
        print("The final grade of", column1[counter], "is", round(finalgrade, 2))
        finalgradelist.append(finalgrade)
        counter = counter + 1


f = open('Mine_GradesFinal.txt', "w")
index = 0
for i in range(0, numrows):
        row = str(column1[index])+ (' ') + str(column2[index])+ (' ') + str(column3[index])+ (' ') + str(column4[index])+ (' ') + str(column5[index])+ (' ') + str(column6[index])+ (' ') + str(round(finalgradelist[index], 2))
        f.write(row)
        f.write("\n")
        index = index + 1

#Find the mean
box = 0
mean = 0
for i in range(0, len(finalgradelist)):
    mean = mean + finalgradelist[box]
    box = box + 1
finalmean = mean/len(finalgradelist)
print('\n')
print("The mean of all your grades is", round(finalmean, 2))

#Find the median
sortedfinalgradelist = sorted(finalgradelist)
if len((finalgradelist)) % 2 == 0:
    i = int(len(finalgradelist)/2)
    y = int(i-1)
    middle = (sortedfinalgradelist)[y] + (sortedfinalgradelist)[i]
    median = middle/2
    print("The median of all your grades is", round(median, 2))
else:
    i = (len(finalgradelist)/2)
    y = math.ceil(i - 1)
    median = sortedfinalgradelist[y]
    print("The median of all your grades is", median)

#Find the variance
bag = 0
variance = 0
for i in range(0, len(finalgradelist)):
    variance = variance + ((finalgradelist[bag]-finalmean)**2)
    bag = bag + 1
finalvariance = variance/(len(finalgradelist))
print(len(finalgradelist))
print("The variance of all your grades is", round(finalvariance, 2))

#Find the standard deviation
standarddeviation = math.sqrt(finalvariance)
print("The standard deviation of all your grades is", round(standarddeviation, 2))
print('\n')

print("The students will be graded with A, B, C, D, E, and F.")
gradeA = int(input("What is the lowest number possible to get an A?"))
gradeB = int(input("What is the lowest number possible to get a B?"))
gradeC = int(input("What is the lowest number possible to get a C?"))
gradeD = int(input("What is the lowest number possible to get a D?"))

ind = 0

for i in range(len(finalgradelist)):
    if finalgradelist[ind] >= gradeA:
        print(column1[ind], " got an A.")
        ind = ind + 1
    elif finalgradelist[ind] < gradeA and finalgradelist[ind] >= gradeB:
        print(column1[ind], " got a B.")
        ind = ind + 1
    elif finalgradelist[ind] < gradeB and finalgradelist[ind] >= gradeC:
        print(column1[ind], " got a C.")
        ind = ind + 1
    elif finalgradelist[ind] < gradeC and finalgradelist[ind] >= gradeD:
        print(column1[ind], " got a D.")
        ind = ind + 1
    elif finalgradelist[ind] < gradeD:
        print(column1[ind], " got a F.")
        ind = ind + 1