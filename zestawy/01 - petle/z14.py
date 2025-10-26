# Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
# jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od
# miliona.

cutoff = 1e6

def is_perfect(n) -> bool:
    sum = 1
    i = 2
    while i*i < n:
        if n % i == 0:
            sum += i + n/i
            if sum > n:
                return False
        i += 1
    if sum == n:
        return True
    return False

for i in range(1, int(cutoff)):
    if is_perfect(i):
        print(i)