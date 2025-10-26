# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

n = int(input("N = "))

a = 1
b = 1
while a <= n:
    a2 = 1
    b2 = 1
    while a2 <= a:
        if a*a2 == n:
            print("TAK", a2, a)
            exit(0)

        b2, a2 = a2 + b2, b2
    b, a = a+b, b

print("NIE")