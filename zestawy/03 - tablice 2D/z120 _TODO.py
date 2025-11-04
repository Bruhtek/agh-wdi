# Zadanie 120. Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
# pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i
# sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
# która zwraca ilość liczb sąsiadujących z 4 liczbami wspolno-czynnikowymi.

primes = []


def generate_primes(n)->None:
    is_prime = [1 for _ in range(n+1)]
    is_prime[0] = 0
    is_prime[1] = 0
    i = 2
    while i*i < n:
        if is_prime[i] == 0:
            continue

        for j in range(i*i, n+1, i):
            is_prime[j] = 0

        if i == 2:
            i += 1
        else:
            i += 2

    prime_count = 0
    for i in range(0, n+1):
        if is_prime[i] == 1:
            prime_count += 1

    global primes
    primes = [0 for _ in range(prime_count)]
    iter = 0
    for i in range(n+1):
        if is_prime[i] == 1:
            primes[iter] = i
            iter += 1


def wspolno_czynnikowe(a, b)->bool:
    return True

def four(tab)->int:
    count = 0
    generate_primes(1e5)

