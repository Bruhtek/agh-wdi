# Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.

def get_primes(n)->list[int]:
    is_prime = [1 for _ in range(n+1)]
    is_prime[0] = 0
    is_prime[1] = 0

    i = 2
    while i*i <= n+1:
        if is_prime[i] == 0:
            if i == 2:
                i += 1
            else:
                i += 2
            continue
        j = i*i
        while j <= n:
            is_prime[j] = 0
            j += i

        if i == 2:
            i += 1
        else:
            i += 2

    primes = [index for (index, num) in enumerate(is_prime) if num == 1]
    return primes

def prime_factors(n)->None:
    primes = get_primes(n)
    for prime in primes:
        while n % prime == 0:
            print(prime)
            n //= prime


prime_factors(33)