# Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek
# stopnia 3.

# Ogólny wzór - a(n+1) = ((n-1)*a(n) + A/(a(n)^(k-1))/k

def quadratic_root(a, max_tries = 1000, max_diff = 1e-12):
    tries = 0
    a_next = a
    while tries < max_tries:
        tries += 1
        res = ((2 * a_next) + (a/(a_next * a_next))) / 3
        if abs(a_next - res) < max_diff:
            print(tries)
            return res
        a_next = res
    print(tries)
    return a_next


print(quadratic_root(27))