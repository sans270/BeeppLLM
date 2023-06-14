x = input("What is your phrase? ")
y = input("What is your other phrase? ")

onephr = list(x)
twophr = list(y)
count = 0
for i in range(len(onephr)):
    if onephr[count] == ' ':
        onephr.remove(' ')
        count = count - 1
    else:
        count = count + 1

index = 0
for j in range(len(twophr)):
    if twophr[index] == ' ':
        twophr.remove(' ')
        index = index - 1
    else:
        index = index + 1

anagram = False
if len(onephr) == len(twophr):
    anagram = True
else:
    anagram = False

if anagram == True:
    for i in range(len(onephr)):
        if onephr[i] in twophr:
            anagram = True
            twophr.remove(onephr[i])
        else:
            anagram = False
            break
else:
    anagram = False

if len(twophr) == 0:
    anagram = True
else:
    anagram = False
    
if anagram == True:
    print("Your phrases are anagrams.")
else:
    print("Your phrases are not anagrams.")