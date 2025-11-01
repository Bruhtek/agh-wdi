# Dwie liczby naturalne większe od 1 są zgodne jeżeli dzielą się przez te same liczby pierwsze.
# Przykładem zgodnych liczb są pary: (6,24),(40,50),(13,169),(44,242),
# nie są zgodne np. pary: (6,8),(40,60),(13,39),(44,99)
# Tablica T została wypełniona liczbami z zakresu [2..999]. Sąsiadami pola o indeksie i w tablicy są pola
# o indeksie j, gdy abs(i−j) < 3. Proszę napisać funkcję zgodne(T), która dla tak wypełnionej tablicy
# zwraca liczbę elementów mających przynajmniej jednego zgodnego sąsiada. Po wykonaniu funkcji tablica
# nie musi pozostać nie zmieniona. Na przykład dla tablicy: T = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]
# funkcja powinna zwrócić wartość 7 (są to liczby 2,4,6,24,12,15,45).

def sito(n)->list[int]:
    pierwsze = [1 for _ in range(n+1)]
    pierwsze[0] = 0
    pierwsze[1] = 0
    i = 2
    while i*i <= n:
        if(pierwsze[i] == 0):
            i += 2
            continue
        for j in range(i*i, n+1, i):
            pierwsze[j] = 0
        if i == 2:
            i += 1
        else:
            i += 2

    pierwsze_count = 0
    for i in range(len(pierwsze)):
        if pierwsze[i] == 1:
            pierwsze_count += 1
    liczby = [0 for _ in range(pierwsze_count)]
    iter = 0
    for i in range(len(pierwsze)):
        if pierwsze[i] == 1:
            liczby[iter] = i
            iter += 1
    return liczby

def zgodne(a, b, pierwsze)->bool:
    bigger = max(a, b)
    for pierwsza in pierwsze:
        if pierwsza > bigger:
            return True
        if a % pierwsza == 0 and b % pierwsza != 0:
            return False
        if b % pierwsza == 0 and a % pierwsza != 0:
            return False
    return True

def friendly_neighbors(tab)->int:
    pierwsze = sito(999)
    count = 0
    n = len(tab)
    for i in range(0, n):
        has_zgoda = False
        neighbor_start = max(0, i-2)
        neighbor_end = min(i+2,n-1) + 1
        for j in range(neighbor_start, neighbor_end):
            if i == j: continue
            if zgodne(tab[i], tab[j], pierwsze):
                has_zgoda = True
                break
        if has_zgoda:
            count += 1
    return count

print(friendly_neighbors([2,3,4,5,7,6,23,24,12,13,14,15,16,45]))