# Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
# obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
import random

def is_prime_fermat(n, tries = 50):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def get_sum(mask, tab1, tab2)->int:
    sum = 0
    iter = 0
    while mask > 0:
        if mask % 2 == 0:
            sum += tab1[iter]
        else:
            sum += tab2[iter]
        mask //= 2
        iter += 1
    return sum

def get_tab_sums(tab1, tab2)->list[int]:
    n = len(tab1) # we are assuming that len(tab1) = len(tab2)
    sums = [0 for _ in range(2**n)]
    for mask in range(2**n):
        sums[mask] = get_sum(mask, tab1, tab2)
    return sums

def main(tab1, tab2)->int:
    sums = get_tab_sums(tab1, tab2)
    count = 0
    for sum in sums:
        if is_prime_fermat(sum):
            print(sum)
            count += 1
    return count

tab1 = [1,3,2,4,5,6,7]
tab2 = [9,7,4,8,5,6,7]

print(main(tab1, tab2))