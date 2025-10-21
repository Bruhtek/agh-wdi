# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
import math
from operator import contains


def same_digits(a, b)->bool:
    digits = []
    while a > 0:
        digit = a % 10
        digits += [digit]
        a //= 10

    while b > 0:
        digit = b % 10
        if not contains(digits, digit):
            return False
        digits.remove(digit)
        b //= 10

    return len(digits) == 0

print(same_digits(321, 123))
print(same_digits(1000, 10000))
print(same_digits(111, 111))