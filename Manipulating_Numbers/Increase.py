import math

num = int(input("Please enter a number: "))

digitlist = []


numdigits = math.floor(math.log(num, 10)+1)
first = math.floor(num/(10**(numdigits-1)))
digitlist.append(first)
x = num % (10**(numdigits-1))
for i in range(0, numdigits-1):
    digit = math.floor(x/(10**(numdigits-(i+2))))
    digitlist.append(digit)
    x = x % (10**(numdigits-(i+2)))


index1 = 0
index2 = 1
increasing = True
for i in range(0, len(digitlist)-1):
    if digitlist[index1] > digitlist[index2]:
        increasing = False
    index1 = index1 + 1
    index2 = index2 + 1

if increasing:
    print("Your number, ", num,  ", has digits that are monotonically increasing.")
else:
    print("Your number, ", num, ", has digits that are not monotonically increasing.")