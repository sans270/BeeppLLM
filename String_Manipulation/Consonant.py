vowel = ['a', 'e', 'i', 'o', 'u']

x = input("What is your word? ")

word = list(x)

num = 0
conslist = []
for z in word:
    if z not in vowel:
        num = num + 1
        conslist.append(z)

if num == 0:
    print("Your word has no consonants.")
else:
    print("Your word has ", num, " consonants. Your consonants are: ", conslist)