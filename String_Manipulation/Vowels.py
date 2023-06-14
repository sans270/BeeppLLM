vowel = ['a', 'e', 'i', 'o', 'u']

x = input("What is your word? ")

word = list(x)

num = 0
vowellist = []
for z in word:
    if z in vowel:
        num = num + 1
        vowellist.append(z)

if num == 0:
    print("Your word has no vowels.")
else:
    print("Your word has ", num, " vowels. Your vowels are: ", vowellist)