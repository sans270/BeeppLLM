num = int(input("What is your number?"))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(num, " factorial is: ", factorial)