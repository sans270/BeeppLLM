import math

print("Please give the two legs of the right triangle of which you would like the hypotenuse.")
a = input("First leg:")
b = input("Second leg:")

r = (float(a) ** 2)+(float(b) ** 2)
c = math.sqrt(r)
print("Your hypotenuse is", c)