# Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania
# ich skrajnych cyfr. Na przykład: 71317 → 131 → 3. Proszę napisać program, który wypisuje wszystkie takie
# liczby mniejsze od N.
import math
import random

def is_prime_fermat(n, tries = 50)->bool:
    if n < 2:
        return False

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False

    return True

def is_palindrome(n)->bool:
    reversed = 0
    n_copy = n
    while n_copy > 0:
        reversed = 10 * reversed + n_copy % 10
        n_copy //= 10

    return reversed == n

def remove_outside_digits(n)->int:
    n //= 10

    if n < 1:
        return 0

    n = n % (10 ** int(math.log10(n)))
    return n

n = int(input("N = "))

for i in range(2, n):
    num = i

    while num > 0:
        if not is_palindrome(num):
            break

        if not is_prime_fermat(num):
            break

        num = remove_outside_digits(num)
    else:
        print(i)
