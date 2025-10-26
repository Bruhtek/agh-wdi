# Dane są ciągi: An+1 = √An ∗ Bn oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do wspól-
# nej granicy nazywanej średnią arytmetyczno-geometryczną. Proszę napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb naturalnych.
import math


def avg_art_geo(a, b, eps = 1e-12):
    while abs(a - b) > eps:
        a,b = math.sqrt(a*b), (a+b)/2

    return a

print(avg_art_geo(4, 4))
print(avg_art_geo(6, 24))