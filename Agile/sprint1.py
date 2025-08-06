import math
a, b, c = 1, -5, 6
d = b**2 - 4*a*c
if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots: {r1}, {r2}")
else:
    print("No real roots")
