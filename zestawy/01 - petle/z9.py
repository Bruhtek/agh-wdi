# Proszę napisać program rozwiązujący równanie xx = 2024 metodą bisekcji.

a = 1
b = 10
target = 2024

eps = 1e-12

def calc(x) -> float:
    return x**x

while b-a>eps:
    mid_point = (a + b)/2
    w = mid_point ** mid_point - target
    if w < 0:
        a = mid_point
    else:
        b = mid_point

print(a, a**a)

