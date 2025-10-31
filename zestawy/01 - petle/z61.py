# Dana jest liczba naturalna N , którą zapisujemy w systemie o podstawie od 2 do 16. Tak
# zapisaną liczbę ”rozcinamy” w dowolnym miejscu na dwa kawałki, a powstałe w ten sposób liczby mnożymy.
# Proszę napisać funkcję, która dla liczby N zwróci najmniejszą podstawę systemu, w którym można uzyskać
# największy iloczyn, a dodatkowo obie liczby powstałe z podziału są względnie pierwsze. Na przykład: liczba
# N = 202 w systemie o podstawie 6 ma postać 534(6). Możliwe podziały w tym systemie o względnie pierw-
# szych czynnikach to: 5(6) ∗34(6) i 53(6) ∗4(6) co w systemie o podstawie 10 odpowiada iloczynom: 5∗22 = 110 i
# 33 ∗ 4 = 132. Ten drugi jest największym możliwym do osiągnięcia, a zatem funkcja powinna zwrócić wartość
# podstawy równą 6.
import math


def to_other_base(n, base)->list[int]:
    tab_size = int(math.log(n, base)) + 1
    tab = [0 for _ in range(tab_size)]
    iter = tab_size-1
    while n > 0:
        tab[iter] = n%base
        iter -= 1
        n //= base

    return tab

def gcd(a, b)->int:
    highest = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            highest = i
    return highest

def to_decimal(tab, orig_base)->int:
    n = len(tab)
    res = 0
    mult = 1
    for i in range(n-1, -1, -1):
        res += tab[i] * mult
        mult *= orig_base
    return res

def split_into_two(tab: list[int])->list[list[list[int]]]:
    n = len(tab)
    options = n - 1
    if options == 0:
        return []

    res = [[0 for _ in range(2)] for _ in range(options)]
    for i in range(1, options + 1):
        res[i-1][0] = tab[:i]
        res[i-1][1] = tab[i:]

    return res


def base_for_max_value(n)->int:
    max_val = 0
    max_base = -1

    for base in range(2, 16):
        n_base = to_other_base(n, base)
        for option in split_into_two(n_base):
            a = to_decimal(option[0], base)
            b = to_decimal(option[1], base)

            if gcd(a, b) == 1:
                mult = a * b
                if mult > max_val:
                    max_val = mult
                    max_base = base

    return max_base

print(base_for_max_value(202))