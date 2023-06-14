numnums = int(input("How many numbers are there to decrypt? "))

numlist = []
for i in range(numnums):
    num = int(input("What is the number? "))
    numlist.append(num)


alphabet = str('abcdefghijklmnopqrstuvwxyz')
listalphabet = list(alphabet)
multipnum = int(input("What number did you multiply to get this encryption? "))
modnum = int(input("What number did you mod to get this encryption? "))

if multipnum < modnum:
    mya = modnum
    myb = multipnum
if multipnum >= modnum:
    mya = multipnum
    myb = modnum

rem = mya % myb
count = 0
remlist = []
remlist.append(myb)
remlist.append(rem)
while rem > 0:
    rem = remlist[count] % remlist[count+1]
    remlist.append(rem)
    count = count + 1
if len(remlist) == 0:
    gcf = myb
else:
    index = len(remlist) - 2
    gcf = remlist[index]

print(gcf)

if gcf == 1:
    for i in range(1, modnum+1):
        inverse = i * multipnum
        if inverse % modnum == 1:
                multipinverse = i
                print(multipinverse)
                break
    declist = []
    for i in range(len(numlist)):
        alphnum = multipinverse * (numlist[i])
        declist.append(alphnum)
    print(declist)

    moddeclist = []
    for i in range(len(declist)):
        r = declist[i] % modnum
        moddeclist.append(r)
    print(moddeclist)
    letterlist = []
    for i in range(len(moddeclist)):
        for d in range(len(listalphabet)+1):
            if moddeclist[i] == d:
                letterlist.append(listalphabet[d-1])


    print("The decryption of your numbers is: ")
    print(letterlist)

else:
    print('\n')
    print("Please enter another number, this one does not work.")