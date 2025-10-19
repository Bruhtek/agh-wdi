# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

def square_root(s, max_tries = 1000, max_diff = 1e-12):
    tries = 0
    a_next = 1
    while tries < max_tries:
        tries += 1
        res = ((s/a_next) + a_next) / 2
        if abs(a_next - res) < max_diff:
            print(tries)
            return res
        a_next = res
    print(tries)
    return a_next


s = float(input("S = "))
print(square_root(s))