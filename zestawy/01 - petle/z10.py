# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def is_fib_mult(n)->bool:
    a = 1
    b = 1

    while a*b < n:
        b, a = b+a, b

    return a*b == n


print(is_fib_mult(2)) # 1*2
print(is_fib_mult(40)) # 5*8