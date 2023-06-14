bag = 0
sumlist = []
for i in range(10,999):
    prime = True
    ones = i%10
    tensones = i%100
    tens = (tensones-ones)/10
    hundredstens = ((i)%1000)
    hundreds = (hundredstens-tensones)/100
    sumdigits = int(ones + tens + hundreds)
    for j in range(2, (sumdigits)):
        if (sumdigits) % j == 0:
            prime = False
    if prime:
        sumlist.append(i)
        bag = bag + 1
sumlist.remove(10)
sumlist.remove(100)
print("Your list is", sumlist, ".")
print("There are", bag, "2 or 3-digit numbers that have a digit sum that is prime")
