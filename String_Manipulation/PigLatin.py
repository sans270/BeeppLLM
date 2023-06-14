z = input("What is your word?")

word = list(z)

vowels = []
vowels.append('a')
vowels.append('e')
vowels.append('i')
vowels.append('o')
vowels.append('u')

if word[0] in vowels:
    word.append('a')
    word.append('y')
    transword = ' '
    for x in word:
        transword += x
    print("Your translated word is: ", transword)
else:
    first = word[0]
    translist = []
    translist.extend(word)
    translist.pop(0)
    translist.append(first)
    translist.append('a')
    translist.append('y')
    finword = ' '
    for x in translist:
        finword += x
    print("Your translated word is: ", finword)
