import math
num = int(input("Please enter a number: "))

numdigits = math.floor(math.log(num, 10))

digitlist = []

previous = num % 10
x = 100
digitlist.append(previous)

for i in range(0, numdigits):
    bignum = num % x
    digit = (bignum - previous)/(x/10)
    digitlist.append(digit)
    x = 10 * x
    previous = bignum

indexf = 0

indexb = (len(digitlist)-1)

palindrome = True

while indexb > indexf:
    if digitlist[indexf] != digitlist[indexb]:
        palindrome = False
    indexf = indexf + 1
    indexb = indexb - 1
if palindrome:
    print("Your number, ", num, ", is a palindrome.")
else:
    print("Your number, ", num, ", is not a palindrome.")