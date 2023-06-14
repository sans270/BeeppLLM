import math
print('\n')
print("This program will find the volume of a backpack made out of half a cylinder on top of a rectangular prism.")

length = float(input("What is the length of the rectangular prism?"))
width = float(input("What is the width of the rectangular prism?"))
height = float(input("What is the height of the rectangular prism?"))
units = input("Which units would you like it in? (centimeters, inches, meters, etc.) ")

rectvol = length*width*height

radius = width/2
cylheight = length

cylvol = ((math.pi)*((radius**2)*(cylheight)))
backcylvol = cylvol/2
totalvol = rectvol + backcylvol

print('\n')
print("Here is the total volume of your backpack, without being rounded: ")
print(totalvol, " square ", units)
print("Here is the total volume of your backpack, rounded to the nearest tenth: ")
print(round(totalvol, 1), " square ", units)
print('\n')