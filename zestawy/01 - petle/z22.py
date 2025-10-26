# Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
# wyrazów ciągu Fibonacciego. Wyznaczyć te ilorazy dla różnych wartości dwóch początkowych wyrazów
# ciągu.

def golden_ratio(a, b, eps = 1e-12)->float:
    phi = b/a
    phi_next = 0
    while abs(phi - phi_next) > eps:
        b, a = a+b, b
        phi = phi_next
        phi_next = b/a

    return phi_next

print(golden_ratio(1, 1))
print(golden_ratio(77, 1))
print(golden_ratio(2, 1))