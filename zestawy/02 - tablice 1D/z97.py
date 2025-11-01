# Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułam-
# ki reprezentowane są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję
# longest(T), zwracającą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geome-
# tryczny. W przypadku, gdy w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość
# 0.
# Przykłady:
# print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
# print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
# print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
# print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcd_frac(frac: tuple[int,int])->tuple[int,int]:
    frac_gcd = gcd(frac[0], frac[1])
    return int(frac[0] / frac_gcd), int(frac[1] / frac_gcd)

def multiply_frac(frac: tuple[int,int], mult)->tuple[int,int]:
    return lcd_frac((frac[0] * mult, frac[1]))

def get_q(frac1, frac2)->float:
    if frac2[1] == 0 or frac1[0] == 0:
        return 1e12
    return (frac2[0]/frac2[1])/(frac1[0]/frac1[1])

def longest(tab: list[tuple[int,int]])->int:
    longest = 0
    n = len(tab)
    if n <= 2:
        return 0
    curr_len = 2
    curr_q = get_q(tab[0], tab[1])
    for i in range(2, n):
        item = lcd_frac(tab[i])
        prev = lcd_frac(tab[i-1])
        if multiply_frac(prev, curr_q) != item:
            if curr_len > longest:
                longest = curr_len
            curr_len = 2
            curr_q = get_q(prev, item)
        else:
            curr_len += 1



    longest = max(longest, curr_len)
    if longest <= 2:
        return 0
    return longest


print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] )) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] )) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] )) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] )) # wypisze 0