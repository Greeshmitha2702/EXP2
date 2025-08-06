import math

def roots(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return r1, r2
    else:
        return None

print("v2: With root calculation")
print(roots(1, -5, 6))