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
print(numrows)

for i in range(1, numrows+1):
    value = (int(column2[hwcounter])+int(column3[hwcounter]))/2
    total = homework*value
    homeworkgradelist.append(total)
    hwcounter = hwcounter + 1
print(homeworkgradelist)
testgradelist = []
testcounter = 0

for i in range(1, numrows+1):
    tvalue = (int(column4[testcounter])+int(column5[testcounter]))/2
    print(tvalue)
    ttotal = tests*tvalue
    print(ttotal)
    testgradelist.append(ttotal)
    testcounter = testcounter + 1
print(testgradelist)
partgradelist = []
partcounter = 0

for i in range(1, numrows+1):
    pvalue = int(column6[partcounter])
    ptotal = participation * pvalue
    partgradelist.append(ptotal)
    partcounter = partcounter + 1
print(partgradelist)

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