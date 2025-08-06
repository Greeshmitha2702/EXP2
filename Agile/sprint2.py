import math

try:
    with open("../data.txt") as f:
        lines = f.readlines()

    for line in lines:
        a, b, c = map(float, line.split())
        d = b**2 - 4*a*c
        if d >= 0:
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
            print(f"Roots for ({a},{b},{c}): {r1}, {r2}")
        else:
            print(f"No real roots for ({a},{b},{c})")
except Exception as e:
    print("Error:", e)
