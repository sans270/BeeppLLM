x=int(input("Enter the number of terms of the Fibonacci sequence that you would like:  "))

y = 0
z = 1
counter = 0
if x == 1:
    print(y)
elif x == 0:
    print("There are no numbers")
elif x >= 2:
    #Prints first two numbers
    print(y)
    print(z)
    #Already printed two numbers, so checks only up until x-2. 
    while counter < (x-2):
        n = y + z
        print(n)
        y = z
        z = n
        counter = counter + 1