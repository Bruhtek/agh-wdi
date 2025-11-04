# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M],
# gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza)
# liczby naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w
# tablicy T2 były uporządkowane niemalejąco.

def przepisz(tab1, tab2)->list[int]:
    n = len(tab1)
    m = n*n #len(tab2)

    iter = 0
    tab_indexes = [0 for _ in range(n)]
    smallest_num = -1
    tab_index_to_inc = -1
    while iter < m:
        for i in range(n):
            if tab_indexes[i] >= n:
                continue
            num = tab1[i][tab_indexes[i]]
            if num < smallest_num or tab_index_to_inc == -1:
                smallest_num = num
                tab_index_to_inc = i
        tab2[iter] = smallest_num
        tab_indexes[tab_index_to_inc] += 1
        tab_index_to_inc = -1
        iter += 1

    return tab2


t1 = [
    [2,2,5,6,11],
    [2,4,8,16,32],
    [1,3,5,7,9],
    [5,10,15,20,25],
    [1,1,2,3,5]
]
t2 = [0 for _ in range(len(t1) * len(t1))]

print(przepisz(t1, t2))