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
quotientlist = []
quotient = mya // myb
quotientlist.append(quotient)
quotient = myb // rem
quotientlist.append(quotient)

slist = []
slist.append(1)
slist.append(0)
tlist = []
tlist.append(0)
tlist.append(1)
s1count = 0
s2count = 1

while rem > 0:
    quotient = remlist[count] // remlist[count+1]
    quotientlist.append(quotient)
    rem = remlist[count] % remlist[count+1]
    remlist.append(rem)
    s = slist[s1count] - (quotientlist[s2count] * slist[s2count])
    slist.append(s)
    t = tlist[s1count] - (quotientlist[s1count] * tlist[s2count])
    tlist.append(t)
    count = count + 1
    s1count = s1count + 1
    s2count = s2count + 1
    
if len(remlist) == 0:
    print("Your GCF is", myb)
else:
    index = len(remlist) - 2
    print("Your GCF is", remlist[index])

print("This is your list of s: ", slist)
print("This is your list of t: ", tlist)