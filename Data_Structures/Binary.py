#Program finds if number is binary or not

x = input("Enter a number: ")
num = list(x)
print(num)
binary = True
for i in range(len(num)):
    if num[i] == '0':
        binary = True
    elif num[i] == '1':
        binary = True
    else:
        binary = False
        break


if binary == True:
    print("Your number is binary.")
else:
    print("Your number is not binary.")