# Zadanie 146. ”Waga” liczby jest określona jako liczba różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

primes = []

def calc_primes(limit = 1000)->None:
    is_prime = [1 for _ in range(limit)]
    is_prime[0] = 0
    is_prime[1] = 0
    i = 2
    while i*i <= limit:
        if is_prime[i] == 1:
            for j in range(i*i, limit, i):
                is_prime[j] = 0
        i += 1

    global primes
    primes = [i for i in range(limit) if is_prime[i] == 1]

def calc_weight(num)->int:
    weight = 0
    for prime in primes:
        if prime > num:
            break
        if num % prime == 0:
            weight += 1
            while num % prime == 0:
                num //= prime
    return weight


def can_be_solved(tab: list[int], iter: int, sums: list[int])->bool:
    n = len(tab)
    if iter >= n:
        return sums[0] == sums[1] == sums[2]

    w = tab[iter]
    iter += 1
    return (can_be_solved(tab, iter, [sums[0] + w, sums[1], sums[2]]) or
            can_be_solved(tab, iter, [sums[0], sums[1] + w, sums[2]]) or
            can_be_solved(tab, iter, [sums[0], sums[1], sums[2] + w]))

def solve(tab: list[int])->bool:
    calc_primes()
    weights = [calc_weight(item) for item in tab]
    sums = [0,0,0]
    return sum(weights) % 3 == 0 and can_be_solved(weights, 0, sums)


tab = [2, 3, 6, 5, 7, 30]
print(tab, solve(tab))
tab = [2, 3, 5, 6, 10, 14, 30, 42, 70]
print(tab, solve(tab))
tab = [2, 3, 5, 7, 11, 13, 13]
print(tab, solve(tab))
tab = [2, 3, 5, 7]
print(tab, solve(tab))