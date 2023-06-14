x = int(input("How many numbers do you want to enter? "))

numlist = []

for i in range(x):
    number = int(input("Enter a number: "))
    numlist.append(number)

bignum = numlist[0]
for z in numlist:
    if z > bignum:
        bignum = z

print("The largest number in your list is ", bignum, ".")