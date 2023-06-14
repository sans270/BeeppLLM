import math

print("Please give the two legs of the right triangle which you would like to see if they are in a Pythagorean triple.")
a = input("First leg:")
b = input("Second leg:")

r = (int(a) ** 2)+(int(b) ** 2)
c = math.sqrt(r)
if c % 1 == 0:
    print("This is a Pythagorean triple, and your hypotenuse is", c)
else:
    print("This is not a Pythagorean triple.")