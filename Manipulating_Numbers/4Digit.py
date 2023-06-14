print("This program will find the number in each of the places of a four digit number.")
fourdigit = int(input("Please enter a four digit number: "))

ones = ((fourdigit)%10)
tensones = ((fourdigit)%100)
tens = (tensones-ones)/10
hundredstens = ((fourdigit)%1000)
hundreds = (hundredstens-tensones)/100
thousandshundreds = ((fourdigit)%10000)
thousands = (thousandshundreds-hundredstens)/1000

print("Your thousands value is", thousands, ", your hundreds value is", hundreds, ", your tens value is", tens, ", and your ones value is", ones)