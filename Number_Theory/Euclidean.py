usera = int(input("What is your first number? "))
userb = int(input("What is your second number? "))

if usera < userb:
    mya = userb
    myb = usera
if usera >= userb:
    mya = usera
    myb = userb

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
    print("Your GCF is", myb)
else:
    index = len(remlist) - 2
    print("Your GCF is", remlist[index])