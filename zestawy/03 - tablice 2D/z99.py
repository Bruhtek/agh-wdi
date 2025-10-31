# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.

def only_odd_digits(num)->bool:
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            return False
        num //= 10
    return True

def in_every_row_at_least_one_odd_digits(tab)->bool:
    for row in tab:
        exists = False
        for item in row:
            exists = exists or only_odd_digits(item)
        if not exists:
            return False

    return True

tab = [
    [2,2,3432,11],
    [2,2,41321,532]
]

print(in_every_row_at_least_one_odd_digits(tab))