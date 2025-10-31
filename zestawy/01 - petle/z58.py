# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
# liczbą pierwszą. Na przykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 ∗ 3 = 3 16 jest
# liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16 = 121(3), 1 ∗ 2 ∗ 1 = 2 W liczbie naturalnej możemy
# dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920. Proszę napisać funkcję, która dla
# danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
# jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
import math
import random


def is_prime_fermat(n, tries = 50)->bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False

    return True

def to_another_base(n, base)->list[int]:
    tab_size = int(math.log(n, base)) + 1
    tab = [0 for _ in range(tab_size)]
    iter = tab_size-1
    while n > 0:
        tab[iter] = n % base
        iter -= 1
        n //= base
    return tab

def mult_digits(tab)->int:
    res = 1
    for item in tab:
        res *= item
    return res

def rotuj_liczbe(n)->list[int]:
    rotation_count = int(math.log10(n)) + 1
    tab = [0 for _ in range(rotation_count)]
    tab[0] = n
    for i in range(1, rotation_count):
        to_front = n % 10
        n //= 10
        n = to_front * (10 ** (rotation_count-1)) + n
        tab[i] = n
    return tab

def is_ilo_pierw(n)->int|None:
    for base in range(2, 17):
        for item in rotuj_liczbe(n):
            new_item = to_another_base(n, base)
            item_mult = mult_digits(new_item)
            if is_prime_fermat(item_mult):
                return base

    return None


print(is_ilo_pierw(13))
print(is_ilo_pierw(16))
print(is_ilo_pierw(1428))