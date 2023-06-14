word = input("What is the word that you would like me to encrypt (lowercase, no spaces)? ")

characters = list(word)

alphabet = str('abcdefghijklmnopqrstuvwxyz')
listalphabet = list(alphabet)

positionlist = []

for i in range(len(characters)):
    for d in range(len(listalphabet)):
        if characters[i] == listalphabet[d]:
            positionlist.append(d)

print("What are the number and the mod you would like to multiply by to encrypt? ")

num = int(input("What is the number you would like to multiply by? "))
mod = int(input("What is the number you would like to mod by? "))

if mod < num:
    mya = num
    myb = mod
if mod >= num:
    mya = mod
    myb = num

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

if mod > 26:
    if gcf == 1:
        encryption = []
        for i in range(len(positionlist)):
            firstnum = (positionlist[i])+1
            multiplynum = firstnum * num
            modnum = multiplynum % mod
            encryption.append(modnum)
        print('\n')
        print("Your encryption by", num, "mod", mod, "is:")
        print(encryption)
    else:
        print('\n')
        print("Please enter the numbers such that they are relatively prime.")
else:
    print('\n')
    print("Please enter a mod that is greater than 26.")