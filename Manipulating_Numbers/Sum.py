sum = int(input("Enter a number."))
bag = 0
sumlist = []
for i in range(10, 999):
    ones = i%10
    tensones = i%100
    tens = (tensones-ones)/10
    hundredstens = ((i)%1000)
    hundreds = (hundredstens-tensones)/100
    if tens + ones + hundreds == sum:
        sumlist.append(i)
        bag = bag + 1

print("Your list is", sumlist, ". There are", bag, "2 or 3-digit numbers that have a digit sum of", sum)