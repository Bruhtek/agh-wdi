# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
# znacza długość najdłuższego, spójnego podciągu geometrycznego

def longest_geo(tab)->int:
    longest = 0
    n = len(tab)
    if n <= 2:
        return n
    current_len = 2
    current_q = tab[1]/tab[0]
    for i in range(2, n):
        item = tab[i]
        prev = tab[i-1]
        if prev * current_q == item:
            current_len += 1
        else:
            longest = max(current_len, longest)
            current_q = item/prev
            current_len = 2

    return max(current_len, longest)


tab = [9,27,81,27,9,3,1]
print(longest_geo(tab))