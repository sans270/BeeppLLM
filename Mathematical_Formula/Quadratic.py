import cmath
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

d = (b**2)-(4*a*c)
w = cmath.sqrt(d)

one = ((-b)+(w))/(2*a)
two = ((-b)-(w))/(2*a)

print("Your factors are", one, "and", two)