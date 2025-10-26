# Nieskończony iloczyn √0.5 ∗ √(0.5 + 0.5 ∗ √0.5) ∗ √(0.5 + 0.5 ∗ √(0.5 + 0.5 ∗ √(0.5 ∗ ... ma
# wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.

import math

def calc_pi()->float:
    result = 1
    a = math.sqrt(1/2)
    while a != 1:
        result *= a
        a = math.sqrt(0.5 + (0.5 * a))

    # result = 2/pi
    return math.pow(result/2, -1)

print(calc_pi())