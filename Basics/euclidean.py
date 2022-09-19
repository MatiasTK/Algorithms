import random


def find_gcd_euclid(a, b):
    if b == 0:
        return (a, 1, 0)

    d, s, t = find_gcd_euclid(b, a % b)

    return (d, t, s - (a // b) * t)


n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
res, w1, w2 = find_gcd_euclid(n1, n2)

print(f"GCD of {n1} and {n2} is:", res)
