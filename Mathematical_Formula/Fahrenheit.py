temp = int(input("What is the temperature in Fahrenheit?"))

numer = (temp-32)

endnum = (numer * (5/9))

cels = round(endnum, 2)
print("The temperature ", temp,  " degrees Fahrenheit in Celsius is: ", cels, " degrees.")