y = input("What is your phrase? ")
x = input("What would you like to search for in the phrase? ")

phrase = list(y)
word = list(x)

pind = 0
wind = 0

poslist = []
inphrase = False
for i in range(len(phrase)):
    if phrase[pind] == word[wind]:
        wind = wind + 1
        pind = pind + 1
        if wind == len(word):
            break
    else:
        pind = pind + 1

if len(word) == wind:
    print(x, "is in the phrase.")
else:
    print(x, "is not in the phrase.")