#Program to find whether an integer is an Armstrong number or not

x = input("Enter a number: ")
numlist = list(x)

power = len(numlist)
val = 0
for i in range(len(numlist)):
    val = val + int(numlist[i])**power

if val == int(x):
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number.")