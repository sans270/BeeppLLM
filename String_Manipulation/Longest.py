#This program finds the longest word in the phrase

y = input("Enter a phrase (no punctuation): ")
phrase = y.split(' ')

longest = 0
otherword = 0
for x in phrase:
    if len(x) > longest:
        longest = len(x)
        longword = x
        

print("Your longest word is ", longword)
print("It is ", longest, "letters long.")
print("There may be other words of the same length. This is the first occuring one.")