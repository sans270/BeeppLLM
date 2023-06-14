print("This program will approximate an adult's height by the length of their femur. ")
gender = int(input("Is the adult a male(type 1) or female(type in 2)? "))
femur = float(input("What is the length of their femur bone in inches? "))



if gender == 1:
    firstpart = femur/0.449
    num = 12.15/0.449
    height = firstpart + num
    print("The height of your adult female is approximately", round(height, 2), "inches")

if gender == 2:
    firstpart = femur/0.432
    num = 10.44/0.432
    height = firstpart + num
    print("The height of your adult male is approximately", round(height, 2), "inches")