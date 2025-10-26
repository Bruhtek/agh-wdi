# Trójką prostokątny o bokach wyrażonych liczbami naturalnymi nazywamy Pitagorejskim.
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej jest mniejsza
# od liczby N wprowadzonej z klawiatury
import math

n = int(input("N = "))

a = 1
b = 1
c2 = 0

for a in range(1, n):
    for b in range(1, n):
        c2 = a * a + b * b

        c = math.isqrt(c2)

        if c*c == c2 and c2 < n*n:
            print(f"{a}^2 + {b}^2 = {c}^2")