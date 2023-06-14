x = input("What is your phrase? ")
let = input("What is your letter? ")

phrase = list(x)

count = 0
for i in range(len(phrase)):
    if phrase[i] == let:
        count = count + 1

print("The letter ", let, " appears ", count, " times in your phrase.")