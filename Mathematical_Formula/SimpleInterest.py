princ = int(input("What is the principal? "))
r = float(input("What is the rate of interest in percent? "))
time = int(input("What is the time of interest in years? "))
rate =  (r / 100)

top = (1 + (rate * time))

intr = (princ * top)
finint = round(intr, 2)

print("Your simple interest is: ", finint, " dollars.")