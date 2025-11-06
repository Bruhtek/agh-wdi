# Zadanie 71. Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy prze-
# skoczyć z pola o indeksie k o npól w prawo jeżeli wartość njest czynnikiem pierwszym liczby T[k]. Napisać
# funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

def generate_primes(limit: int)->list[int]:
    is_prime = [1 for _ in range(limit+1)]
    is_prime[0] = 0
    is_prime[1] = 0

    i = 2
    while i*i <= limit:
        if is_prime[i] == 0:
            i += 2
            continue

        for j in range(i*i, limit+1, i):
            is_prime[j] = 0
        if i == 2:
            i += 1
        else:
            i += 2

    prime_count = 0
    for i in range(limit+1):
        if is_prime[i] == 1:
            prime_count += 1
    primes = [0 for _ in range(prime_count)]
    iter = 0
    for i in range(limit+1):
        if is_prime[i] == 1:
            primes[iter] = i
            iter += 1

    return primes


def can_go_to_the_end(tab: list[int])->bool:
    k = len(tab)
    primes = generate_primes(k)

    steps_to_field = [-1 for _ in range(k)]
    steps_to_field[0] = 0
    for i in range(k):
        if steps_to_field[i] == -1:
            continue
        for prime in primes:
            if prime + i >= k:
                break
            can_go = tab[prime+i] % prime == 0
            if can_go:
                # print("Can go from ", i, "(", tab[i], ")", "to", prime + i, "(", tab[prime + i], ")", "moving", prime,
                #       "steps")
                if steps_to_field[prime+i] != -1:
                    steps_to_field[prime+i] = min(steps_to_field[prime+i], steps_to_field[i]+1)
                else:
                    steps_to_field[prime+i] = steps_to_field[i]+1

    # print(steps_to_field)
    return steps_to_field[k-1] != -1


tab = [0,1,2,3,4,5,6,7,8,9,10,11,12,20]
print(can_go_to_the_end(tab))