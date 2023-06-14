y = input("What is your word? ")
x = input("What is your 2nd word? ")

word1 = list(y)
word2 = list(x)
print(word1)
print(word2)

w1ind = 0
w2ind = 0

poslist = []
for i in range(len(word1)):
    if word1[w1ind] == word2[w2ind]:
        poslist.append(word1[w1ind])
        w2ind = w2ind + 1
        w1ind = w1ind + 1
        if w2ind == len(word2):
            break
    else:
        w1ind = w1ind + 1
        w2ind = 0
        break

prefix = ' '

for x in poslist:
    prefix += x

print("Your longest common prefix is: ", prefix)