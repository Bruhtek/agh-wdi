# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
# znacza długość najdłuższego, spójnego podciągu arytmetycznego.

def longest_art(tab)->int:
    longest = 0
    n = len(tab)
    if n <= 2:
        return n
    current_r = tab[1] - tab[0]
    current_len = 2
    for i in range(2, n):
        previous = tab[i-1]
        item = tab[i]
        if previous + current_r == item:
            current_len += 1
        else:
            if current_len > longest:
                longest = current_len
            current_len = 2
            current_r = item - previous

    if current_len > longest:
        longest = current_len

    return longest

tab = [1,2,3,4,7,14,42,49,20,19,18,17,16,15]
print(longest_art(tab))