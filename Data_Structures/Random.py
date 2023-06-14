import random

firstlist = []
x = input("How many 2-digit random numbers do you want to print in your first list?")

for i in range(0, int(x)):
    firstlist.append(random.randint(10, 99))
print("This is your first list: ", firstlist)
secondlist = []

y = input("How many 2-digit random numbers do you want to print in your second list?")

for i in range(0, int(y)):
    secondlist.append(random.randint(10, 99))
print("This is your second list: ", secondlist)

biglist = firstlist + secondlist
print("Here is both of your lists combined and sorted from least to greatest:")

biglist.sort()
print(biglist)