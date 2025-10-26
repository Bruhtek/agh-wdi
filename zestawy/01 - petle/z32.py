# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest
# równy 2.

def is_multiple_of(n)->bool:
    a = 2
    while a <= n:
        if n % a == 0:
            return True
        a = 3 * a + 1

    return False

n = int(input("N = "))

print(n, is_multiple_of(n))