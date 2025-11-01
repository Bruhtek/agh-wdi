# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
# znacza długość najdłuższego, spójnego podciągu rosnącego.

def longest_rising(tab)->int:
    rising_start = -1
    rising_longest = 0
    previous = 0
    n = len(tab)
    for i in range(n):
        item = tab[i]
        if item > previous or i == 0:
            if rising_start == -1:
                rising_start = i - 1
        else:
            rising_len = i - rising_start
            rising_start = -1
            if rising_longest < rising_len:
                rising_longest = rising_len
        previous = item
    return rising_longest

tab = [24,7,1,2,3,4,23,6,7,8,123,1,2,3,4,-5]
print(longest_rising(tab))

