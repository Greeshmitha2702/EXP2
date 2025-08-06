import math

def quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        return None

def main():
    try:
        with open("../data.txt", "r") as file:
            numbers = list(map(float, file.read().split()))

        for i in range(0, len(numbers), 3):
            a, b, c = numbers[i:i+3]
            roots = quadratic_roots(a, b, c)
            if roots:
                print(f"Roots for ({a}, {b}, {c}): {roots[0]}, {roots[1]}")
            else:
                print(f"No real roots for ({a}, {b}, {c})")

    except Exception as e:
        print("Error:", e)

main()