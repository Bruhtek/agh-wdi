# Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
# najmniejszej różnicy. Na przykład: 30 = 5 ∗ 6, 120 = 10 ∗ 12.
import math

n = int(input("N = "))

best_diff = n-1
best_a = 1

for a in range(1, math.isqrt(n)+1):
    if n % a == 0:
        b = n // a
        diff = b - a
        if diff < best_diff:
            best_diff = diff
            best_a = a

print(n, "=", best_a, "*", n // best_a)