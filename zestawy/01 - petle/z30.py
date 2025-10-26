# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

n = int(input("N = "))

def is_multiply_of_an(n)->bool:
    for i in range(1, n):
        a = i*i + i + 1
        if n % a == 0:
            return True

    return False

print(is_multiply_of_an(n))