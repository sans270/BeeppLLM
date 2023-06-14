num = int(input("What is your number?"))

primelist = []
for i in range(2, num):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        primelist.append(i)

index = 0
primefactorization = []

numprime = True

for j in range(2, num):
    if num % j == 0:
        numprime = False

if numprime:
    print("Your number", num, "is already prime, so your prime factorization is:")
    print("1 *", num)

if numprime == False:
    while num > 1:
        if num % primelist[index] == 0:
                primefactorization.append(primelist[index])
                num = num / primelist[index]
        index = index + 1
    print("Your prime factorization is:")
    print(num)
    print("*")
    primeindex = 0
    for i in range(len(primefactorization)):
        print(primefactorization[primeindex])
        print("*")
        primeindex = primeindex + 1