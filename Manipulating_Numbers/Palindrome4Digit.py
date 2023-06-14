fourdigit = int(input("Please enter a four digit number: "))

ones = ((fourdigit)%10)
tensones = ((fourdigit)%100)
tens = (tensones-ones)/10
hundredstens = ((fourdigit)%1000)
hundreds = (hundredstens-tensones)/100
thousandshundreds = ((fourdigit)%10000)
thousands = (thousandshundreds-hundredstens)/1000

firstlast = False
middles = False

if ones == thousands:
    firstlast = True
    if tens == hundreds:
        middles = True
    else:
        print("Your number is not a palindrome")
else: 
    print("Your number is not a palindrome.")

if firstlast:
    if middles:
        print("Your number, ", fourdigit, ", is a palindrome.")
