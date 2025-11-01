# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwraca-
# jącą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
# jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
# wartości).

def min_val(tab)->int:
    min = tab[0]
    for item in tab:
       if item < min:
           min = item
    return min

def max_val(tab)->int:
    max = tab[0]
    for item in tab:
        if item > max:
            max = item
    return max

def exactly_one_min_max(tab)->bool:
    miniVal = min_val(tab)
    maxiVal = max_val(tab)

    mini_count = 0
    maxi_count = 0
    for item in tab:
        if item == miniVal:
            mini_count += 1
        if item == maxiVal:
            maxi_count += 1
    return mini_count == 1 and maxi_count == 1


tab = [1,2,3,4,5,6]
print(exactly_one_min_max(tab))
tab_2 = [1,2,3,4,3,2,1]
print(exactly_one_min_max(tab_2))