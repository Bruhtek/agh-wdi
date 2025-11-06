# Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
# wartości prawdopodobieństwa dla N z zakresu 20-40.
import random


def has_two_same_number(tab)->bool:
    n = len(tab)
    for i in range(n):
        first = tab[i]
        for j in range(1, n-i):
            if (first == tab[i+j]):
                return True
    return False

def fill_with_dob(size: int)->list[int]:
    tab = [random.randint(1,365) for _ in range(size)]
    return tab


tries = 1000
for n in range(20, 41):
    count = 0
    for _ in range(tries):
        tab = fill_with_dob(n)
        if has_two_same_number(tab):
            count += 1
    print(f"Probability for {n} people: {count*100/tries}%")