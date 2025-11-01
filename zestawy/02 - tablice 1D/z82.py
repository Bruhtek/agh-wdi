# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def sum_tab_from_to(tab, from_index, to_index)->int:
    sum = 0
    for i in range(from_index, to_index+1):
        sum += tab[i]
    return sum

def sum_indexes_from_to(from_index, to_index)->int:
    count = to_index - from_index + 1
    return ((from_index + to_index)/2) * count

def is_range_growing(tab, from_index, to_index)->bool:
    previous = tab[from_index]
    for i in range(from_index+1, to_index+1):
        item = tab[i]
        if item <= previous:
            return False
        previous = item
    return True

def longest_growing(tab)->int:
    longest = 0
    n = len(tab)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if is_range_growing(tab, i, j):
                sum_val = sum_tab_from_to(tab, i, j)
                sum_ind = sum_indexes_from_to(i, j)
                if sum_val == sum_ind:
                    longest = max(longest, j - i + 1)

    return longest

tab_1 = [5,4,3,2,1,0,6,7,8]
print(longest_growing(tab_1))