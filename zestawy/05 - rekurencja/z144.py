# Zadanie 144. Korzystając z zależności: n po k = n−1 po k-1 + n-1 po k
# proszę napisać funkcję obliczającą wartość
# symbolu Newtona dla argumentów n i k.

def newtonsBinomial(n, k)->int:
    if n == k or k == 1:
        return 1
    if k == 1:
        return n
    if n == k+1:
        return n

    return newtonsBinomial(n-1, k-1) + newtonsBinomial(n-1, k)

print(newtonsBinomial(5,2))