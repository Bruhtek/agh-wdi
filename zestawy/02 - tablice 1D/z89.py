# Zadanie 89. Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory
# cyfr występujące w liczbie są identyczne. Na przykład:
# 13 = 31(4) i 23 = 113(4)
# 18 = 102(4) i 33 = 201(4)
# 107 = 1223(4) i 57 = 321(4).
# Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca długość naj-
# dłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych

def to_quatenary(n)->int:
    res = 0
    mult = 1
    while n > 0:
        res += (n%4) * mult
        mult *= 10
        n //= 4
    return res

def are_digits_identical(a,b)->int:
    digits_a = [0 for _ in range(10)]
    while a > 0:
        digits_a[a%10] = 1
        a //= 10

    digits_b = [0 for _ in range(10)]
    while b > 0:
        digits_b[b%10] = 1
        b //= 10

    for i in range(10):
        if digits_a[i] != digits_b[i]:
            return False
    return True

def longest_subseq(tab: list[int])->int:
    longest = 1
    n = len(tab)
    for i in range(0, n-1):
        a = to_quatenary(tab[i])
        curr_len = 1
        for j in range(i+1, n):
            b = to_quatenary(tab[j])
            if are_digits_identical(a, b):
                curr_len += 1
        longest = max(longest, curr_len)
    return longest


print(longest_subseq([13,13,107,57,57,13,57,107]))