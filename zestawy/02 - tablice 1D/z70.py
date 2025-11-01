# Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
import random


def only_odd_digits(n)->bool:
    while n > 0:
        digit = n % 10
        n //= 10
        if digit % 2 == 0:
            return False
    return True

def check_tab(T)->bool:
    for item in T:
        if only_odd_digits(item):
            return True
    return False

def fill_tab(T)->list[int]:
    n = len(T)
    for i in range(n):
        T[i] = random.randint(1, 1000)
    return T

if __name__ == "__main__":
    tab = [0 for _ in range(20)]
    tab = fill_tab(tab)
    print(tab)
    print(check_tab(tab))