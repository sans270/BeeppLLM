import numpy as geek
import random

firstlist = []
secondlist = []

x = int(input("How many numbers do you want to be in your vectors?"))

firstvector = geek.random.rand(x)
print("This is your first vector:")
print(firstvector)

secondvector = geek.random.rand(x)
print("This is your second vector:")
print(secondvector)

sumvectors = firstvector + secondvector

print("This is the sum of your two vectors:")
print(sumvectors)