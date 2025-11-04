# W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
# fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
# poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy odszuka ten
# fragment i zwróci jego długość.

def in_fib(a, b)->bool:
    if a > b:
        a, b = b, a
    x = 1
    y = 1
    while x < a and x < b:
        y, x = x+y, y

    return x == a and y == b

tab = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,2,1,1],
    [1,1,3,1,1],
    [1,1,1,1,1]
]

