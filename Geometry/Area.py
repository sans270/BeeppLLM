import math

print("This program calculates the area of a regular 2D polygon when given the amount of sides that it has and a side length.")
x = input("How many sides does your polygon have?")
y = input("What is a side length of your polygon?")
n = ((1/2)*(int(y)))
deg = ((1/2))*(360/int(x))
s = math.radians(deg)
d = (math.tan(s))
a = (n/d)
area = (1/2)*(int(y)*int(x))*(a)

print("Your area is", area, "units squared")