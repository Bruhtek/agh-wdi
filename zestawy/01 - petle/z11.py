# Proszę napisać funkcje sprawdzający czy zadana liczba jest pierwszą
import random


def is_prime(n, tries = 100) -> bool:
    if n < 2:
        return False

    for _ in range(tries):
        a = random.randint(1, n-1)
        # a ^ n-1 % n
        if pow(a, n-1, n) != 1:
            return False
    return True


print(2, is_prime(2))
print(3, is_prime(3))
print(41, is_prime(41))
print(2137, is_prime(2137))