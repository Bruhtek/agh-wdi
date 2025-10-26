# Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych.

def gcd(a, b, c)->int:
    greatest = 1

    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c

    for i in range(1, smallest+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            greatest = i

    return greatest


print(gcd(28,14,40))