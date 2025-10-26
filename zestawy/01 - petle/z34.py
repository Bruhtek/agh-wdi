# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg geometryczny.

def are_nums_geo(n)->bool:
    a1 = n % 10
    a2 = (n // 10) % 10
    q = a2/a1

    n //= 100
    while n > 0:
        a2 = a2 * q
        if a2 != n % 10:
            return False
        n //= 10
    return True

print(are_nums_geo(1248))
print(are_nums_geo(139))
print(are_nums_geo(931))
print(are_nums_geo(123))