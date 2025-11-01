# Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
# liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
import random


def is_prime_fermat(n, tries=50)->bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False

    return True


def fits_condition(tab)->bool:
    n = len(tab)
    a, b = 1,2
    while a < n:
        item_to_check = tab[a]
        tab[a] = -1
        if is_prime_fermat(item_to_check) or item_to_check < 2:
            return False
        a, b = b, a+b

    for i in range(n):
        item = tab[i]
        if item == -1:
            continue
        if is_prime_fermat(item):
            return True

    return False


# fib: 1,1,2,3,5,8
tab = [1,12,24,15,17,12]
print(fits_condition(tab))