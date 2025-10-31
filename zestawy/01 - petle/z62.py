# Dwie liczby naturalne A, B można ”skleić” ze sobą jeżeli 2 lub 3 ostatnie cyfry liczby A
# pookrywają się z odpowiednio z pierwszymi 2 lub 3 cyframi liczby B. Na przykład: 2571 i 710, 12345678
# i 678999. Siła z jaką sklejone są liczby to liczba złożona z dopasowanych cyfr, dla powyższych przykładów
# to odpowiednio: 71 i 678. Dany jest cykl złożony z N 8 cyfrowych liczb, zawarty w tablicy T . Proszę
# napisać funkcję, która w takim cyklu znajdzie fragment o największej, sumarycznej sile sklejenia. Funk-
# cja powinna zwrócić siłę sklejenia znalezionego cyklu. W przypadku gdy żadnych dwóch kolejnych liczb nie
# uda się skleić, funkcja powinna zwrócić wartość 0. Jeżeli uda się skleić cały cykl funkcja powinna zwrócić −1.
# Dla tablicy: T = [79000023, 23111134, 55555555, 66666104, 10467700, 88888879]
# Funkcja powinna zwrócić wartość 104 (elementy o indeksach 3,4),
import math


# first, the combined number, second, the power, -1 on first if it cannot be sticked
def stick(a, b)->tuple[int,int]:
    last_2_a = a % 100
    last_3_a = a % 1000

    b_len = int(math.log10(b)) + 1
    first_2_b = b // (10 ** (b_len - 2))
    first_3_b = b // (10 ** (b_len - 3))

    if (first_3_b == last_3_a):
        new_res = (a // 1000) * (10 ** b_len) + b
        return new_res, last_3_a
    elif (first_2_b == last_2_a):
        new_res = (a // 100) * (10 ** b_len) + b
        return new_res, last_2_a

    return -1, 0

def max_sticky(tab)->int:
    n = len(tab)
    max_combined_pow = 0
    for i in range(n):
        a = tab[i]
        iter = i + 1
        power = 0
        while iter < n:
            b = tab[iter]
            stick_res = stick(a, b)
            if stick_res[0] == -1:
                break
            power += stick_res[1]
            a = stick_res[0]
            if power > max_combined_pow:
                max_combined_pow = power
            if i == 0 and iter == n-1:
                return -1
            iter += 1

    return max_combined_pow


print(max_sticky([79000023, 23111134, 55555555, 66666104, 10467700, 88888879]))