x = input("What is your phrase? (no capital letters) ")

phrase = list(x)

alph = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alph)

count = 0

for i in range (len(phrase)):
    if phrase[count] in alphabet:
        alphabet.remove(phrase[count])
        print(alphabet)
        count = count + 1
    else:
        count = count + 1

if len(alphabet) == 0:
    print("Your phrase contains all of the letters of the alphabet.")
else:
    print("Your phrase does not contain all of the letters of the alphabet.")
    letnum = 26-len(alphabet)
    print("Your phrase contains", letnum, "letters of the alphabet.")