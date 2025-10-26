# Dwie różne liczby nazywamy zaprzyjaźnionymi gdy każda jest równa sumie podzielników
# właściwych drugiej liczby, na przykład 220 i 284. Proszę napisać program wyszukujący liczby zaprzyjaźnione
# mniejsze od miliona.

def sp(n) -> int:
    sum = 1
    i = 2
    while i*i < n:
        if n % i == 0:
            sum += i + n//i
        i += 1
    if i*i == n:
        sum += i
    return sum

for a in range(1, int(1e6)):
    b = sp(a)
    if b < a and sp(b) == a:
        print(a, b)