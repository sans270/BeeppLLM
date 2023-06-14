x = int(input("What is the temperature in Celsuis?"))

top = (x*(9/5))
noround = (top + 32)

fahren = round(noround, 2)
print("The temperature ", x,  " degrees Celsius in Fahrenheit is: ", fahren, " degrees.")