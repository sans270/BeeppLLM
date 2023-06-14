import random

#Making first random list
firstlist = []
x = input("How many 2-digit random numbers do you want to print in your first list?")
    #Generating the random list
for i in range(0, int(x)):
    firstlist.append(random.randint(10, 99))
print("This is your first list: ", firstlist)

#Making second random list
secondlist = []
y = input("How many 2-digit random numbers do you want to print in your second list?")
    #Generating random list
for i in range(0, int(y)):
    secondlist.append(random.randint(10, 99))
print("This is your second list: ", secondlist)

#Combining two lists
biglist = firstlist + secondlist

#SORTING LIST:
print("Here is both of your lists combined and sorted from least to greatest:")

sortedlist = []
#Loop that finds the smallest number in the current list, adds it to sorted list, removes it from big list.
for i in range(len(biglist)):
    #Loop that finds smallest number
    small = biglist[0]
    for j in biglist:
        if j < small:
            small = j
    #Removing and adding it to new sorted list
    sortedlist.append(small)
    biglist.remove(small)
print(sortedlist)