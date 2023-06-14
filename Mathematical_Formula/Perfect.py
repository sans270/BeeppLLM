number = int(input("Enter a number: "))

factorlist = []
for i in range(1, number + 1):
    if number % i == 0:
        factorlist.append(i)
del factorlist[len(factorlist)-1]

sum = 0
for f in range(len(factorlist)):
    sum = sum + factorlist[f]

if sum == number:
    print("Your number is a perfect number")
else:
    print("Your number is not a perfect number")