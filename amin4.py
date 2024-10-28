import math
a = 3
b = 6
c = 9
discriminant = b*b - 4.0*a*c
if discriminant < 0:
    print("no real roots")
else:
    D = math.sqrt(discriminant)
    print(((-b + d) / 2.0))
    print(((-b - d) / 2.0))